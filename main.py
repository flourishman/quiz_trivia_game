import json
import os
import random

FILENAME = "questions.json"


def save_file(questions):
    try:
        with open(FILENAME, "w") as file:
            json.dump(questions, file, indent=4)
        print("Questions saved successfully!")
    except OSError:
        print("Error saving questions to file.")


def load_file():
    if not os.path.exists(FILENAME):
        return []
    try:
        with open(FILENAME, "r") as file:
            return json.load(file)
    except (json.JSONDecodeError, OSError):
        return []


def add_questions(questions):
    print("\n--- ADD NEW QUESTION ---")
    question = input("Type in the new question: ").strip()

    options = []
    for option_num in range(1, 5):
        opt = input(f"Enter option {option_num}: ").strip()
        options.append(opt)

    while True:
        answer = input(
            "Enter the correct answer (must match one of the options above): "
        ).strip()
        if answer in options:
            break
        print("Error: Answer must exactly match one of the options above!")

    questions.append(
        {
            "question": question,
            "option": options,
            "answer": answer,
        }
    )

    save_file(questions)


def play_game(questions):
    if not questions:
        print("\nNo questions found! Please add some questions first.")
        return

    # Work on a copy so we don't modify the main list permanently
    game_questions = questions.copy()
    random.shuffle(game_questions)

    score = 0

    for q in game_questions:
        print(f"\n{q['question']}")

        # Shuffle a copy of options so answer position varies
        options = q["option"].copy()
        random.shuffle(options)

        for idx, option in enumerate(options, 1):
            print(f"{idx}. {option}")

        while True:
            try:
                user_choice = int(input("Enter option number (1-4): "))

                if 1 <= user_choice <= len(options):
                    selected_answer = options[user_choice - 1]

                    if selected_answer == q["answer"]:
                        print("Correct!")
                        score += 1
                    else:
                        print(f"Wrong! The correct answer was: {q['answer']}")
                    break

                print(
                    f"Invalid option number. Please enter a number from 1 to {len(options)}."
                )

            except ValueError:
                print("Error! Please enter a valid number.")

    print(f"\nGame Over! You scored: {score} out of {len(game_questions)}")


def main():
    print("Welcome to Quiz / Trivia Game")
    questions = load_file()

    while True:
        print("\n--- MAIN MENU ---")
        print("1. Play Game")
        print("2. Add Question")
        print("3. Exit")

        user_choice = input("Enter your choice: ").strip()

        if user_choice == "1":
            play_game(questions)
        elif user_choice == "2":
            add_questions(questions)
        elif user_choice == "3":
            print("Thank you for playing!")
            break
        else:
            print("Invalid choice, please enter 1, 2, or 3.")


if __name__ == "__main__":
    main()