"""
RECORD CHECK  -  my version
===========================

Name  : Munashe Michael Mapara
Lane  :  Cyber       (delete two)
Date  :

Run it:   python template.py

Work through the numbered sections in order. Each one tells you what it must do.
Delete these instructions as you replace them with your code.
"""

# FUNCTIONS
def status_of(percent):
    """Returns the status string based on the given percentage threshold."""
    if percent >= 100.0:
        return "OVER LIMIT"
    elif percent >= 90.0:
        return "WARNING"
    else:
        return "OK"

def check(value, limit):
    """Calculates and returns the difference and percentage based on value and limit."""
    difference = value - limit
    percent = (value / limit) * 100.0
    return difference, percent

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



over_limit_count = 0

# Sections 2-4 in a loop
while True:
    print("\n--- NEW RECORD CHECK (Type 'quit' to exit) ---")
    
    # 2. INPUT
    label = input("Enter the text label: ")
    if label.lower() == "quit":
        break
        
    value = float(input("Enter the value: "))
    limit = float(input("Enter the limit: "))

    # 3. PROCESS
    # call check() to get difference and percentage
    difference, percent = check(value, limit)
    
    # call status_of() to get the status string
    status = status_of(percent)
    
    if status == "OVER LIMIT":
        over_limit_count += 1

    # 4. OUTPUT
    # call print_report() instead of printing directly here
    print_report(label, value, limit, difference, percent, status)



# This runs ONCE after the user types "quit" to exit the loop
print("\n" + "=" * 34)
print(f"TOTAL OVER LIMIT:      {over_limit_count:>10d}")
print("=" * 34)

