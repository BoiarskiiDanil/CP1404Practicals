import random
MIN_POSSIBLE_SCORE = 0
PASS_SCORE_THRESHOLD = 50
EXCELLENT_SCORE_THRESHOLD = 90
MAX_POSSIBLE_SCORE = 100


def main():
    # score = float(input("Enter score: "))
    random_score = random.randint(0, 100)
    print_result(random_score)


def print_result(random_score):
    if random_score > MAX_POSSIBLE_SCORE or random_score < MIN_POSSIBLE_SCORE:
        print("Invalid score")
    elif random_score >= EXCELLENT_SCORE_THRESHOLD:
        print(random_score, "is Excellent")
    elif random_score >= PASS_SCORE_THRESHOLD:
        print(random_score, "is Passable")
    else:
        print(random_score, "is Bad")


main()
