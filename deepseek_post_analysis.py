#!/usr/bin/env python3
# deepseek_post_analysis.py
# PromptPressure Post-Analysis Script
# Version: 1.5.0-patch9
# Generated: 2025-06-14
# Notable: Aggregates all CSVs in outputs/ and runs Deepseek analysis; serializes payload correctly; logs errors generically

import os
import sys
import glob
from datetime import datetime
from dotenv import load_dotenv
from adapters.lmstudio_adapter import generate_response
import pandas as pd

# Load environment variables and set up error log
load_dotenv()
ERROR_LOG_FILE = os.getenv("ERROR_LOG", "error_log")

# 1) Auto-discover any CSV files in this directory
pattern = "*.csv"
matches = glob.glob(pattern)
if not matches:
    message = f"[{datetime.utcnow().isoformat()}] No files matching '{pattern}' found in {os.getcwd()}"
    with open(ERROR_LOG_FILE, "a", encoding="utf-8") as logf:
        logf.write(message + "\n")
    print(message)
    sys.exit(1)

# 2) Read and aggregate all CSVs
combined_frames = []
for csv_file in matches:
    try:
        df = pd.read_csv(csv_file)
        combined_frames.append(df)
    except Exception as e:
        message = f"[{datetime.utcnow().isoformat()}] Failed to read '{csv_file}': {e}"
        with open(ERROR_LOG_FILE, "a", encoding="utf-8") as logf:
            logf.write(message + "\n")
        continue

# 3) Concatenate and run analysis
combined_df = pd.concat(combined_frames, ignore_index=True)
# Extract model_name or fallback
if "model_name" in combined_df.columns and not combined_df["model_name"].empty:
    model_name = combined_df["model_name"].iloc[0]
else:
    model_name = os.getenv("DEEPSEEK_MODEL_NAME")

# Prepare JSON-serializable payload
payload = combined_df.to_dict(orient="records")

try:
    analysis = generate_response(payload, model_name)
except Exception as e:
    message = f"[{datetime.utcnow().isoformat()}] Analysis generation failed: {e}"
    with open(ERROR_LOG_FILE, "a", encoding="utf-8") as logf:
        logf.write(message + "\n")
    print(message)
    sys.exit(1)

# 4) Save analysis result to disk
out_path = "deepseek_post_analysis.txt"
try:
    with open(out_path, "w", encoding="utf-8") as f:
        f.write(analysis)
    print(f"[✓] Deepseek analysis saved to '{out_path}'")
except Exception as e:
    message = f"[{datetime.utcnow().isoformat()}] Failed to write analysis file: {e}"
    with open(ERROR_LOG_FILE, "a", encoding="utf-8") as logf:
        logf.write(message + "\n")
    print(message)
    sys.exit(1)
