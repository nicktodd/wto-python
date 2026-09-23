"""Load step: write the reporting-ready outputs."""
import json
import logging
from datetime import datetime, timezone

import pandas as pd

log = logging.getLogger(__name__)


def write_outputs(df, summary, out_dir, metadata):
    # TODO: Create out_dir. Write df to trade_reporting.csv, and an Excel workbook
    # trade_reporting.xlsx with sheets: data, exports_by_region_bn (summary), metadata.
    # Write metadata.json including the row count and a UTC timestamp.
    # Log what was written and return (csv_path, xlsx_path).
    raise NotImplementedError
