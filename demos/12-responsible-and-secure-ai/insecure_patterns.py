"""Insecure patterns AI assistants often write.

Discussion file: DO NOT RUN. All hosts are
fictitious (example.org / example.com).
"""
import logging
import os
import sqlite3

import requests

# 1. Secret hard-coded in source code
API_KEY = "sk-live-EXAMPLE-NOT-A-REAL-KEY"

# 1. Fix: read it from the environment
API_KEY = os.environ["STATS_API_KEY"]

# 2. TLS certificate checks disabled
resp = requests.get(
    "https://stats.example.org/tariffs",
    verify=False)

# 3. SQL built from user input
name = input("Country: ")
db = sqlite3.connect("trade.db")
sql = f"SELECT * FROM t WHERE c = '{name}'"
rows = db.execute(sql).fetchall()

# 3. Fix: a parameterised query
rows = db.execute(
    "SELECT * FROM t WHERE c = ?",
    (name,)).fetchall()

# 4. Personal data written to a log file
contact = {"name": "Delegate 01",
           "email": "delegate01@example.org"}
logging.info("Sent to %s", contact)

# 5. Confidential data sent to an
#    unapproved external AI service
requests.post(
    "https://free-ai.example.com/summarise",
    json={"text": open("draft.txt").read()})

# 6. Running text as code
rule = input("Filter: ")
result = eval(rule)
