"""
RECORD CHECK  -  my version
===========================

Name  : Munashe Michael Mapara
Lane  :   Cyber      (delete two)
Date  :

Run it:   python template.py

Work through the numbered sections in order. Each one tells you what it must do.
Delete these instructions as you replace them with your code.
"""

# Keep track of how many items go over the limit
over_limit_count = 0

#  loop to check as many records as you like
while True:
    print("\n--- NEW RECORD CHECK (Type 'quit' to exit) ---")
    
    
    # 1. Ask for three values.
    label = input("Enter the text label: ")
    
    # Check if the user wants to stop the program
    if label.lower() == "quit":
        break
        
    value = float(input("Enter the value: "))
    limit = float(input("Enter the limit: "))

   
    # 2. Work out the difference and the percentage.
    difference = value - limit
    
    
    percent = (value / limit) * 100.0

    # 3. Decide a status based on the percentage.
    #  "OVER LIMIT" (100%+), "WARNING" (90%+), otherwise "OK"
    if percent >= 100.0:
        status = "OVER LIMIT"
        over_limit_count += 1  # Increment the counter
    elif percent >= 90.0:
        status = "WARNING"
    else:
        status = "OK"

    
    # Print the report inside a border.
    print()
    print("=" * 34)
    print(f"  RECORD CHECK  -  {label}")
    print("=" * 34)

    # Original values given, plus status
    print(f"Label:                 {label:>10s}")
    print(f"Value:                 {value:>10.2f}")
    print(f"Limit:                 {limit:>10.2f}")
    
    # Add difference and percent, 2 decimal places, right-aligned
    print(f"Difference:            {difference:>+10.2f}")
    print(f"Percentage:            {percent:>10.2f}%")
    print(f"Status:                {status:>10s}")
    
    print("=" * 34)


# This runs ONCE after the user types "quit" to exit the loop
print("\n" + "=" * 34)
print(f"TOTAL OVER LIMIT:      {over_limit_count:>10d}")
print("=" * 34)
