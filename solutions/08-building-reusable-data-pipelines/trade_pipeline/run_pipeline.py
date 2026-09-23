"""Run the trade pipeline end to end.

Run from the folder that contains trade_pipeline/ :
    python -m trade_pipeline.run_pipeline
    python -m trade_pipeline.run_pipeline --offline --verbose
"""
import argparse
import logging
import sys
from pathlib import Path

from . import config
from .extract import extract_wb, read_countries, read_raw_trade
from .load import write_outputs
from .transform import add_indicators, add_reference_data, clean_trade, summarise, validate

log = logging.getLogger("trade_pipeline")


def setup_logging(out_dir, verbose=False):
    out_dir.mkdir(parents=True, exist_ok=True)
    logging.basicConfig(
        level=logging.DEBUG if verbose else logging.INFO,
        format="%(asctime)s %(levelname)-7s %(name)s: %(message)s",
        handlers=[logging.StreamHandler(), logging.FileHandler(out_dir / "pipeline.log")],
    )


def parse_args(argv=None):
    p = argparse.ArgumentParser(description="Build a reporting-ready trade dataset.")
    p.add_argument("--out", type=Path, default=config.DEFAULT_OUT, help="output folder")
    p.add_argument("--offline", action="store_true", help="use cached API responses only")
    p.add_argument("--verbose", action="store_true", help="debug logging")
    return p.parse_args(argv)


def run(out_dir, offline=False):
    raw = read_raw_trade()
    countries = read_countries()
    trade = add_reference_data(clean_trade(raw), countries)

    wb = extract_wb(sorted(trade["iso3"].unique()), config.START_YEAR, config.END_YEAR, offline)
    report = add_indicators(trade, wb)

    problems = validate(report)
    if problems:
        raise ValueError(f"Validation failed: {problems}")
    log.info("Validation passed: %d rows", len(report))

    metadata = {
        "trade_source": config.RAW_TRADE_FILE.name + " (illustrative)",
        "indicator_source": config.WB_BASE,
        "indicators": {k: v[0] for k, v in config.WB_INDICATORS.items()},
        "offline": offline,
    }
    return write_outputs(report, summarise(report), out_dir, metadata)


def main(argv=None):
    args = parse_args(argv)
    setup_logging(args.out, args.verbose)
    log.info("Pipeline started (offline=%s)", args.offline)
    try:
        run(args.out, args.offline)
    except Exception:
        log.exception("Pipeline failed")
        return 1
    log.info("Pipeline finished")
    return 0


if __name__ == "__main__":
    sys.exit(main())
