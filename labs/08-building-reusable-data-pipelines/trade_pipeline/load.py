"""Load step: write the reporting-ready outputs."""
import json
import logging
from datetime import datetime, timezone

import pandas as pd

log = logging.getLogger(__name__)


def write_outputs(df, summary, out_dir, metadata):
    # TODO STEP 9: create out_dir; write df to trade_reporting.csv; write
    # trade_reporting.xlsx with sheets data, exports_by_region_bn (summary) and
    # metadata; write metadata.json including "rows" and a UTC timestamp.
    # Return (csv_path, xlsx_path).
    raise NotImplementedError
