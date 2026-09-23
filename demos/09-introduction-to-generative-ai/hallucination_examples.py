"""Plausible-looking AI output: a discussion file.

Each block LOOKS right. Each one is wrong.
Do not run this file; it is for review only.
"""
import pandas as pd

df = pd.read_csv("../../data/trade_summary.csv")

# 1. Invented function: pandas has no
#    read_worldbank(). It sounds plausible.
gdp = pd.read_worldbank("NY.GDP.MKTP.CD")

# 2. Invented endpoint and parameters. The
#    real WTO API is documented at
#    apiportal.wto.org and needs a key.
url = ("https://api.wto.org/v1/trade"
       "?reporter=KEN&year=2023&format=csv")

# 3. Runs, but the logic is wrong: asked for
#    total 2023 exports, it returns the mean.
total_2023 = df[df["year"] == 2023][
    "exports_usd_m"].mean()

# 4. A confident, invented "fact".
# Kenya joined the WTO in 2001.
# (Kenya has been a member since 1995.)

# 5. Outdated API: DataFrame.append() was
#    removed in pandas 2.0. Use pd.concat().
df = df.append({"reporter": "Test"},
               ignore_index=True)
