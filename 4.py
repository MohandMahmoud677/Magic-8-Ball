import random

def get_user_question():
    print("Ask the Magic 8 Ball a question (or press Enter to exit): ")
    question = input().strip()
    return question if question else None

def get_random_response():
    responses = [
        "Yes, definitely!",
        "No, I don't think so.",
        "Maybe, time will tell.",
        "I can't predict now.",
        "Ask again later.",
        "The answer is unclear, try again.",
        "Chances are very low.",
        "Absolutely!",
        "Don't count on it.",
        "The answer is uncertain."
    ]
    return random.choice(responses)

def display_response(response):
    print(f"🎱 The Magic 8 Ball says: {response}")

def play_again():
    print("Do you want to play again? (yes/no): ")
    choice = input().strip().lower()
    return choice == "yes" or choice == "y"

def magic_8_ball():
    print("🎱 Welcome to the Magic 8 Ball game! 🎱")
    while True:
        question = get_user_question()
        if question is None:
            print("Goodbye!")
            break
        response = get_random_response()
        display_response(response)
        if not play_again():
            print("Thanks for playing! See you next time! 👋")
            break

if _name_ == "_main_":
    magic_8_ball()
