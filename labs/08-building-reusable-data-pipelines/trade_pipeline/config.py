"""Configuration for the trade pipeline. Change settings here, not in the code."""
from pathlib import Path

ROOT = Path(__file__).resolve().parents[3]          # repository root
DATA = ROOT / "data"
CACHE = DATA / "cache"
DEFAULT_OUT = Path(__file__).resolve().parent / "output"

RAW_TRADE_FILE = DATA / "trade_raw_2019_2023.csv"
COUNTRIES_FILE = DATA / "countries.xlsx"

WB_BASE = "https://api.worldbank.org/v2"
WB_INDICATORS = {
    # output column: (World Bank code, cached response file)
    "gdp_usd": ("NY.GDP.MKTP.CD", "wb_gdp_usd.json"),
    "exports_pct_gdp_wb": ("NE.EXP.GNFS.ZS", "wb_exports_pct_gdp.json"),
}
START_YEAR, END_YEAR = 2019, 2023
TIMEOUT_SECONDS = 30

NAME_MAP = {
    "USA": "United States", "U.S.": "United States", "united states": "United States",
    "UK": "United Kingdom", "U.K.": "United Kingdom",
    "Vietnam": "Viet Nam",
    "germany": "Germany", "Federal Republic of Germany": "Germany",
}
PERIOD_FORMATS = ["%Y-%m-%d", "%d/%m/%Y", "%b %Y", "%Y"]
