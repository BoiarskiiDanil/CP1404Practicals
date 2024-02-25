MIN_POSSIBLE_SCORE = 0
PASS_SCORE_THRESHOLD = 50
EXCELLENT_SCORE_THRESHOLD = 90
MAX_POSSIBLE_SCORE = 100
MENU = """G - Get a valid score
    P - Print result
    S - Show stars
    Q - Quit"""
print(MENU)


def main():
    choice = input(">>> ").upper()
    score = int(input("Enter score: "))
    while choice != "Q":
        if choice == "G":
            get_valid_score(score)
        elif choice == "P":
            print_result(score)
        elif choice == "S":
            show_stars(score)
        else:
            print("Invalid option")
        print(MENU)
        choice = input(">>> ").upper()
    print("Farewell.")


def get_valid_score(score):
    if score < 0 or score > 100:
        print("Invalid score")
        score = int(input("Enter score: "))
    return score


def print_result(score):
    if score > MAX_POSSIBLE_SCORE or score < MIN_POSSIBLE_SCORE:
        print("Invalid score")
    elif score >= EXCELLENT_SCORE_THRESHOLD:
        print(score, "is Excellent")
    elif score >= PASS_SCORE_THRESHOLD:
        print(score, "is Passable")
    else:
        print(score, "is Bad")


def show_stars(score):
    for i in range(score):
        print("*")


main()
