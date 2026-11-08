"""
RECORD CHECK  -  my version
===========================

Name  : Munashe Michael Mapara
Lane  :  Cyber     (delete two)
Date  :

Run it:   python template.py

Work through the numbered sections in order. Each one tells you what it must do.
Delete these instructions as you replace them with your code.
"""

import os

# FUNCTIONS
def check_record(value, limit):
    """Calculates difference, percentage, and determines status from value and limit."""
    difference = value - limit
    
   
    percent = (value / limit) * 100.0
    
    if percent >= 100.0:
        status = "OVER LIMIT"
    elif percent >= 90.0:
        status = "WARNING"
    else:
        status = "OK"
        
    return difference, percent, status

def print_report(label, value, limit, difference, percent, status):
    """Prints a neatly formatted record report inside a stylized border layout."""
    print()
    print("=" * 34)
    print(f"  RECORD CHECK  -  {label}")
    print("=" * 34)
    print(f"Label:                 {label:>10s}")
    print(f"Value:                 {value:>10.2f}")
    print(f"Limit:                 {limit:>10.2f}")
    print(f"Difference:            {difference:>+10.2f}")
    print(f"Percentage:            {percent:>10.2f}%")
    print(f"Status:                {status:>10s}")
    print("=" * 34)

def load_records(path):
    """Reads label, value, and limit lines from a file and returns a list of dicts."""
    loaded_list = []
    with open(path, "r") as file:
        for line in file:
            # Strip whitespace and skip empty lines
            cleaned_line = line.strip()
            if not cleaned_line:
                continue
            
            # Split line by comma
            parts = cleaned_line.split(",")
            if len(parts) == 3:
                loaded_list.append({
                    "label": parts[0].strip(),
                    "value": float(parts[1]),
                    "limit": float(parts[2])
                })
    return loaded_list

def save_results(path, results):
    """Writes the finalized results to a file, one line per record."""
    with open(path, "w") as file:
        for record in results:
            file.write(f"{record['label']},{record['status']}\n")


# ====================================================================== STORE
# 2. Get your records into a list of dicts.
# load records using the function.
data_filename = "records.txt"
output_filename = "results.txt"

records = load_records(data_filename)



# 3. Loop over records. For each one, call check_record and print_report.
over_limit_count = 0
results_to_save = []

for record in records:
    # Unpack the dict data
    lbl = record["label"]
    val = record["value"]
    lim = record["limit"]
    
    # Process
    diff, pct, stat = check_record(val, lim)
    
    # tracking
    if stat == "OVER LIMIT":
        over_limit_count += 1
        
    # Append to our saving buffer
    results_to_save.append({"label": lbl, "status": stat})
    
    # Output
    print_report(lbl, val, lim, diff, pct, stat)

# Save results out to a file
save_results(output_filename, results_to_save)

# Print total count once loop ends
print("\n" + "=" * 34)
print(f"TOTAL OVER LIMIT:      {over_limit_count:>10d}")
print("=" * 34)
