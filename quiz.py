def run_quiz():
    # Список глобальных и простых вопросов
    questions = [
        {
            "prompt": "What is the main brain of a computer?",
            "options": ["A) Monitor", "B) Keyboard", "C) CPU (Processor)", "D) Mouse"],
            "answer": "C"
        },
        {
            "prompt": "Which of these is a popular search engine?",
            "options": ["A) Google", "B) Photoshop", "C) Spotify", "D) Minecraft"],
            "answer": "A"
        },
        {
            "prompt": "What does 'WWW' stand for in a website address?",
            "options": ["A) World Wide Web", "B) Wild Wild West", "C) World War Win", "D) Website World Wide"],
            "answer": "A"
        },
        {
            "prompt": "Which device is used to type text on a computer?",
            "options": ["A) Printer", "B) Keyboard", "C) Camera", "D) Speaker"],
            "answer": "B"
        }
    ]

    score = 0

    print("--- Welcome to the Beginner IT Quiz! ---")
    print("Test your knowledge and have fun!")

    for q in questions:
        print("\n" + q["prompt"])
        for option in q["options"]:
            print(option)

        user_answer = input("Your answer (A, B, C, or D): ").strip().upper()

        if user_answer == q["answer"]:
            print("Excellent! Correct answer.")
            score += 1
        else:
            print(f"Oops! The correct answer was {q['answer']}.")

    # Финальный результат
    print("\n" + "="*30)
    print("QUIZ COMPLETED!")
    print(f"Your final score: {score} out of {len(questions)}")

    if score == len(questions):
        print("Amazing! You are a natural tech genius! 🚀")
    elif score >= len(questions) // 2:
        print("Well done! You have a good handle on the basics! 👍")
    else:
        print("Good effort! Keep learning and you'll get there! ✨")
    print("="*30)


if __name__ == "__main__":
    run_quiz()
