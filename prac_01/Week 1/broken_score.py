"""
CP1404/CP5632 - Practical
"""

MIN_POSSIBLE_SCORE = 0
PASS_SCORE_THRESHOLD = 50
EXCELLENT_SCORE_THRESHOLD = 90
MAX_POSSIBLE_SCORE = 100

score = float(input("Enter score: "))
if score >= PASS_SCORE_THRESHOLD:
    if score > MAX_POSSIBLE_SCORE:
        print("Invalid score")
    elif score >= EXCELLENT_SCORE_THRESHOLD:
        print("Excellent")
    else:
        print("Passable")
elif score < PASS_SCORE_THRESHOLD:
    if score < MIN_POSSIBLE_SCORE:
        print("Invalid score")
    else:
        print("Bad")