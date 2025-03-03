"""
CP1404/CP5632 - Practical
"""

is_finished = False
while not is_finished:
    try:
        result = int(input("Enter a valid integer: "))
        is_finished = True  # Set is_finished to True if input is a valid integer
    except ValueError:  # Catch ValueError when input cannot be converted to an integer
        print("Please enter a valid integer.")
print("Valid result is:", result)