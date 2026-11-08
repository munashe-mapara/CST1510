"""
RECORD CHECK  -  my version
===========================

Name  : Munashe Michael Mapara
Lane  : Cyber     (delete two)
Date  :

Run it:   python template.py

Work through the numbered sections in order. Each one tells you what it must do.
Delete these instructions as you replace them with your code.
"""

import os

# CLASS
class Record:
    """Represents a metric monitoring entry tracking values against defined limits."""
    
    # Excellent: Class-level running total attribute
    over_limit_count = 0

    def __init__(self, label, value, limit):
        """Initializes a new Record instance with a label, value, and threshold limit."""
        self.label = label
        self.value = value
        self.limit = limit

    def status(self):
        """Calculates percentage and returns a status string string based on thresholds."""
        # Leaving potential zero-division active as per your experimental rules
        percent = (self.value / self.limit) * 100.0
        
        if percent >= 100.0:
            # Stretch Goal: Track right on the class object instead of an outside loop counter
            Record.over_limit_count += 1
            return "OVER LIMIT"
        elif percent >= 90.0:
            return "WARNING"
        else:
            return "OK"


#RECORDS
def load_records(path):
    """Reads lines from a data file and returns a list of instantiated Record objects."""
    loaded_objects = []
    
    # Safeguard check to ensure your app behaves gracefully if the path goes missing
    if not os.path.exists(path):
        print(f"Warning: Data file could not be found at {path}")
        return loaded_objects

    with open(path, "r") as file:
        for line in file:
            cleaned_line = line.strip()
            if not cleaned_line:
                continue
            
            parts = cleaned_line.split(",")
            if len(parts) == 3:
                # Instantiate direct Record objects instead of standard raw dicts
                new_record = Record(
                    label=parts[0].strip(),
                    value=float(parts[1]),
                    limit=float(parts[2])
                )
                loaded_objects.append(new_record)
    return loaded_objects



# This ensures VS Code tracks the text file locally right from your current workspace directory!
script_directory = os.path.dirname(os.path.abspath(__file__))
data_filepath = os.path.join(script_directory, "records.txt")

# Load elements via helper function 
records = load_records(data_filepath)


# ==================================================================== OUTPUT
# 3. Print a report for each record object instance
for record in records:
    # Trigger calculations internally on the object state via methods
    current_status = record.status()
    difference = record.value - record.limit
    percent = (record.value / record.limit) * 100.0

    print()
    print("=" * 34)
    print(f"  RECORD CHECK  -  {record.label}")
    print("=" * 34)

    # formatted attributes using object dot notation
    print(f"Label:                 {record.label:>10s}")
    print(f"Value:                 {record.value:>10.2f}")
    print(f"Limit:                 {record.limit:>10.2f}")
    print(f"Difference:            {difference:>+10.2f}")
    print(f"Percentage:            {percent:>10.2f}%")
    print(f"Status:                {current_status:>10s}")

    print("=" * 34)

# Print class-level total tally directly pulled off the class object namespace
print("\n" + "=" * 34)
print(f"TOTAL OVER LIMIT:      {Record.over_limit_count:>10d}")
print("=" * 34)
