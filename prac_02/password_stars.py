def main():
    password = get_password()

def get_password():
    stars_count = int(input("Number of stars: "))
    for i in range(stars_count + 1):
        print_asterisks(i)
    print()

def print_asterisks(password):
    print("*" * password)

main()