"""
CP1404/CP5632 Practical
Quick Pick Lottery Ticket Generator
"""

import random

# Constants for the lottery rules
NUMBERS_PER_PICK = 6
MIN_NUMBER = 1
MAX_NUMBER = 45


def main():
    """Generate and display quick pick lottery tickets."""
    num_picks = int(input("How many quick picks? "))

    for _ in range(num_picks):
        quick_pick = generate_quick_pick()
        print(format_quick_pick(quick_pick))


def generate_quick_pick():
    """Generate a single quick pick with unique random numbers."""
    quick_pick = []
    while len(quick_pick) < NUMBERS_PER_PICK:
        number = random.randint(MIN_NUMBER, MAX_NUMBER)
        if number not in quick_pick:  # Ensure uniqueness
            quick_pick.append(number)
    return sorted(quick_pick)  # Sort the numbers


def format_quick_pick(quick_pick):
    """Format quick pick numbers with proper spacing."""
    return " ".join(f"{num:2}" for num in quick_pick)


main()
