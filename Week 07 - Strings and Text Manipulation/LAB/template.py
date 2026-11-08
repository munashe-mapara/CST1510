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

def parse_line(raw_line):
    """Cleans a messy, inconsistently spaced line and extracts components into a dict."""
    # Remove leading/trailing line spacing and split by commas
    parts = raw_line.strip().split(",")
    
    # 1. Parse the Label (clean spacing and set to standard lowercase/titlecase if desired)
    label = parts[0].strip().upper() # Standardizing to UPPERCASE for system names
    
    # 2. Extract value (split on '=' and grab the number side)
    value_part = parts[1].split("=")[1]
    value = float(value_part.strip())
    
    # 3. Extract limit (split on '=' and grab the number side)
    limit_part = parts[2].split("=")[1]
    limit = float(limit_part.strip())
    
    return {"label": label, "value": value, "limit": limit}

def status_of(value, limit):
    """Evaluates percentage load and returns an operation status tag."""
    percent = (value / limit) * 100.0
    
    if percent >= 100.0:
        return "OVER LIMIT"
    elif percent >= 90.0:
        return "WARNING"
    else:
        return "OK"



#Dynamic script tracking and loading with an external file loop
script_directory = os.path.dirname(os.path.abspath(__file__))
data_filepath = os.path.join(script_directory, "messy_records.txt")

raw_records = []

# Verify file exists before reading to avoid crashes
if os.path.exists(data_filepath):
    with open(data_filepath, "r") as file:
        for line in file:
            # Skip genuinely empty lines
            if line.strip():
                raw_records.append(line)
else:
    print(f"Warning: File not found at {data_filepath}. Creating dummy test values.")
    # Fallback inline list matching the specified prompt shape
    raw_records = [
        "  Srv-01 , used=87 , total=100  ",
        "SRV-02,    used=95,total=100",
        "  srv-03  ,  used=45  ,  total=50  ",
        "Srv-04,used=120,total=100",
        "   SRV-05   ,   used=89   ,   total=100   "
    ]


total_records = 0
flagged_count = 0

print(f"{'CLEANED LABEL':<15} | {'VALUE':<6} | {'LIMIT':<6} | {'STATUS':<10}")
print("-" * 52)

for raw_record in raw_records:
    # 1. Parse out the messy string data using our parsing module
    
    record_dict = parse_line(raw_record)
    
    # 2. Typical: Call status tracking evaluation
    status = status_of(record_dict["value"], record_dict["limit"])
    
    # 3. Increment counters
    total_records += 1
    if status in ["OVER LIMIT", "WARNING"]:
        flagged_count += 1
        
    # Standardized Terminal Display Output
    print(f"{record_dict['label']:<15} | {record_dict['value']:<6.1f} | {record_dict['limit']:<6.1f} | {status:<10}")

# Final metrics compilation log statement summary line
print("-" * 52)
print(f"SUMMARY: Processed {total_records} records. Flagged items: {flagged_count}")
print("-" * 52)
