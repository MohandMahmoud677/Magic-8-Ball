def play_again():
    while True:
        choice = input("Do you want to ask another question? (yes/no): ").strip().lower()
        if choice == "yes":
            return True
        elif choice == "no":
            print("Thanks for playing! Goodbye!")
            return False
        else:
            print("Please type 'yes' or 'no'.")
