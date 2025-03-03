"""
CP1404/CP5632 Practical
List Exercises
"""

def main():
    """Run both exercises: Basic list operations and Security checker."""
    numbers = get_numbers(5)
    display_number_info(numbers)
    security_checker()


def get_numbers(count):
    """Prompt the user for `count` numbers and return them as a list."""
    numbers = []
    for i in range(count):
        number = float(input(f"Number {i + 1}: "))
        numbers.append(number)
    return numbers


def display_number_info(numbers):
    """Display statistics about the list of numbers."""
    print(f"The first number is {numbers[0]}")
    print(f"The last number is {numbers[-1]}")
    print(f"The smallest number is {min(numbers)}")
    print(f"The largest number is {max(numbers)}")
    print(f"The average of the numbers is {sum(numbers) / len(numbers):.1f}")


def security_checker():
    """Check if a user is authorised based on a predefined list of usernames."""
    usernames = [
        'jimbo', 'giltson98', 'derekf', 'WhatSup', 'NicolEye', 'swei45', 
        'BaseInterpreterInterface', 'BaseStdIn', 'Command', 'ExecState', 
        'InteractiveConsole', 'InterpreterInterface', 'StartServer', 'bob'
    ]
    
    username = input("\nEnter your username: ")
    if username in usernames:
        print("Access granted")
    else:
        print("Access denied")


main()
