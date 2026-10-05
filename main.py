import json
import os
import random

print("Welcome to Quiz / Trivia Game")


def play_game(questions):
    
    score = 0
    for q in questions:
        if not questions:
            print("there is no questions in the file")
            break
        
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
    
questions = []
    
def add_questions():
    question = input("Type in the new question: ")
    
    if options <= 4:
        options = input("Enter answer options: ")
        
    answer = input("Enter correct answer from the options: ")
    
    questions.append({
        "question": question,
        "option": options,
        "answer": answer,
    })
    
FILENAME = 'questions.json'

def save_file():
    try:
        with open(FILENAME, 'w') as file:
            return json.dump(questions, file, indent=4)
    except:
        print("Empty file")
    
def load_file():
    if not os.path.exists(FILENAME):
        return []
    try:
        with open(FILENAME, 'r') as file:
            return json.load(file)
    except(json.JSONDecodeError, OSError):
        return []
    
def main():
    questions = load_file()
 
    while True:
        game = [
            "1. Play Game",
            "2. View file content",
            "3. Add content to file",
            "4. Exit",
        ]

        for choice in game:
            print(choice)

        user_choice = input("Enter your choice: ").strip()

        if user_choice == "1":
            random.shuffle(questions)
            play_game(questions)
        elif user_choice == "2":
            load_file(questions)
        elif user_choice == "3":
            add_questions()
        elif user_choice == "4":
            print("Thank you!")
            break
        else:
            print("Invalid user input, enter correct one")


if __name__ == "__main__":
    main()
        
    