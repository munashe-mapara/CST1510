"""
RECORD CHECK  -  my version
===========================

Name  : Munashe Michael Mapara
Lane  :  Cyber      (delete two)
Date  :

Run it:   python template.py

Work through the numbered sections in order. Each one tells you what it must do.
Delete these instructions as you replace them with your code.
"""

import os
import matplotlib.pyplot as plt
import pandas as pd

# Automatically locate the file in the script's local directory to avoid errors
script_directory = os.path.dirname(os.path.abspath(__file__))
csv_filepath = os.path.join(script_directory, "data.csv")
output_csv_filepath = os.path.join(script_directory, "results.csv")
chart_filepath = os.path.join(script_directory, "status_counts.png")

#  LOAD
# 1. Read your data file with pd.read_csv()
df = pd.read_csv(csv_filepath)


# ================================================================= PROCESS
# 2. Add calculated metrics as vectorized column additions
df["percent"] = (df["value"] / df["limit"]) * 100.0

# Categorize status tags using an element-wise lambda function via .apply()
df["status"] = df["percent"].apply(
    lambda pct: "OVER LIMIT" if pct >= 100.0 else ("WARNING" if pct >= 90.0 else "OK")
)


# OUTPUT
# 3. Print the DataFrame & specialized metrics.

print("--- FULL DATAFRAME ---")
print(df)
print("\n" + "=" * 50 + "\n")

# Filter down to non-"OK" rows using a clean boolean mask inside []
print("--- ATTENTION REQUIRED (NOT OK) ---")
filtered_df = df[df["status"] != "OK"]
print(filtered_df)
print("\n" + "=" * 50 + "\n")

# Aggregation counting grouped categories
print("--- COUNTS PER STATUS ---")
status_counts = df.groupby("status").size()
print(status_counts)

# Save the full tracking results back out to a fresh CSV file
df.to_csv(output_csv_filepath, index=False)

#  Build, format, and save a bar chart visualization matrix
plt.figure(figsize=(6, 4))
status_counts.plot(kind="bar", color=["green", "red", "orange"])
plt.title("Record Distribution by Metric Status")
plt.xlabel("Status Category")
plt.ylabel("Count")
plt.tight_layout()
plt.savefig(chart_filepath)
plt.close()

print(f"\n[Success] Analysis completed. Results saved to '{output_csv_filepath}' and chart to '{chart_filepath}'.")
y column your code refers to actually exists - watch case
