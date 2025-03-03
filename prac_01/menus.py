MENU = """(H)ello
(G)oodbye
(Q)uit"""
user_name = input("Enter name: ")
print(MENU)
menu_choice = input(">>> ").upper()
while menu_choice != "Q":
    if menu_choice == "H":
        print("Hello,", user_name)
        print(MENU)
        menu_choice = input(">>> ").upper()
    elif menu_choice == "G":
        print("Goodbye,", user_name)
        print(MENU)
        menu_choice = input(">>> ").upper()
    else:
        print("Invalid choice")
        print(MENU)
        menu_choice = input(">>> ").upper()
print("Finished.")