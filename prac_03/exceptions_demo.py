"""
CP1404/CP5632 - Practical
Answer the following questions:
1. When will a ValueError occur?
A ValueError will occur if the user inputs a value for the numerator or denominator
that cannot be converted to an integer. This includes any input that is not a valid
integer, such as a string of letters or special characters.

2. When will a ZeroDivisionError occur?
A ZeroDivisionError will occur if the denominator is zero, as division by zero is
undefined in mathematics and will cause the program to raise this error.

3. Could you change the code to avoid the possibility of a ZeroDivisionError?
Yes, you can change the code to include a loop that checks if the denominator is zero.
If it is zero, the program will prompt the user to re-enter a non-zero value for the
denominator. This way, division by zero is avoided entirely.
"""

try:
    numerator = int(input("Enter the numerator: "))
    denominator = int(input("Enter the denominator: "))
    fraction = numerator / denominator
    print(fraction)
except ValueError:
    print("Numerator and denominator must be valid numbers!")
except ZeroDivisionError:
    print("Cannot divide by zero!")
print("Finished.")