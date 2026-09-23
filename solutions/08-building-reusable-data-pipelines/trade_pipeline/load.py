"""Load step: write the reporting-ready outputs."""
import json
import logging
from datetime import datetime, timezone

import pandas as pd

log = logging.getLogger(__name__)


def write_outputs(df, summary, out_dir, metadata):
    out_dir.mkdir(parents=True, exist_ok=True)

    csv_path = out_dir / "trade_reporting.csv"
    df.to_csv(csv_path, index=False)

    xlsx_path = out_dir / "trade_reporting.xlsx"
    with pd.ExcelWriter(xlsx_path) as writer:
        df.to_excel(writer, sheet_name="data", index=False)
        summary.to_excel(writer, sheet_name="exports_by_region_bn")
        pd.DataFrame(list(metadata.items()), columns=["item", "value"]).to_excel(
            writer, sheet_name="metadata", index=False)

    metadata = {**metadata, "rows": len(df),
                "created_utc": datetime.now(timezone.utc).isoformat(timespec="seconds")}
    (out_dir / "metadata.json").write_text(json.dumps(metadata, indent=2, default=str),
                                           encoding="utf-8")
    log.info("Wrote %s, %s and metadata.json", csv_path.name, xlsx_path.name)
    return csv_path, xlsx_path
