import json
import os
import random

print("Welcome to Quiz / Trivia Game")


def play_game(questions):
    score = 0

    for q in questions:
        print(q["question"])
        for idx, option in enumerate(q["option"], 1):
            print(f"{idx}. {option}")

        while True:
            try:
                user_choice = int(input("Enter option number (1-4): "))
                if 1 <= user_choice <= len(q["option"]):
                    selected_answer = q["option"][user_choice - 1]
                    if selected_answer == q["answer"]:
                        print("Correct!")
                        score += 1
                    else:
                        print(f"Wrong! The correct answer was: {q['answer']}")
                    break
                print("Invalid option number. Please enter a number from 1 to 4.")
            except ValueError:
                print("Error! Please enter a valid number.")

    print(f"\nGame Over! You scored: {score} out of {len(questions)}")


def main():
    questions = [
        {
            "question": "What color is Nigeria flag?",
            "option": ["Green White Green", "Red", "Blue", "Black"],
            "answer": "Green White Green",
        },
        {
            "question": "Who is the head of the family?",
            "option": ["Mother", "Boy", "Father", "Uncle"],
            "answer": "Father",
        },
    ]

    while True:
        game = [
            "1. Play Game",
            "2. Exit",
        ]

        for choice in game:
            print(choice)

        user_choice = input("Enter your choice: ").strip()

        if user_choice == "1":
            play_game(questions)
        elif user_choice == "2":
            print("Thank you!")
            break
        else:
            print("Invalid user input, enter correct one")


if __name__ == "__main__":
    main()
        
    