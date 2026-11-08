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


# 1. Ask the user for three values.

label = input("Enter the text label (name, hostname, or IP): ")
first = float(input("Enter the first number: "))
second = float(input("Enter the second number: "))


# 2. Work out what you were NOT given.

difference = first - second

# Handle the edge case where the second number is 0 to avoid a ZeroDivisionError
if second != 0.0:
    percent = (first / second) * 100.0
else:
    percent = 0.0


# 3. Print the report.

print()
print("=" * 34)
print(f" RECORD CHECK - {label}")
print("=" * 34)

# Values right-aligned to 10 spaces, 2 decimal places
print(f"First Value:           {first:>10.2f}")
print(f"Second Value:          {second:>10.2f}")

#  Difference always shows its sign (+ or -)
print(f"Difference:            {difference:>+10.2f}")
print(f"Percentage:            {percent:>10.2f}%")

# custom line 
status = "POSITIVE" if difference >= 0 else "NEGATIVE"
print(f"Status:                {status:>10s}")

print("=" * 34)
