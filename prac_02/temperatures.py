MENU = """C - Convert Celsius to Fahrenheit
    F - Convert Fahrenheit to Celsius
    Q - Quit"""
print(MENU)


def main():
    choice = input(">>> ").upper()
    while choice != "Q":
        if choice == "C":
            cels_fahr_conversion()
        elif choice == "F":
            fahr_cels_conversion()
        else:
            print("Invalid option")
        print(MENU)
        choice = input(">>> ").upper()
    print("Thank you.")


def cels_fahr_conversion():
    celsius = float(input("Celsius: "))
    fahrenheit = celsius * 9.0 / 5 + 32
    print(f"Result: {fahrenheit:.2f} F")


def fahr_cels_conversion():
    fahrenheit = float(input("Fahrenheit: "))
    celsius = 5 / 9 * (fahrenheit - 32)
    print(f"Result: {celsius:.2f} C")


main()
