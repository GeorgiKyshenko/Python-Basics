import random

questions = ["Question: What currency is used in Switzerland?", "Question: What is the color of the sky?"]
questions_asked = []
correct_answers = 0
wrong_answers = 0

while len(questions) != 0:
    current_question = random.choice(questions)

    if current_question not in questions_asked:
        print(current_question)
        questions_asked.append(current_question)
        questions.remove(current_question)

    if current_question == "Question: What currency is used in Switzerland?":
        print("A: USD, B: EURO, C: CHF", "D: TRY")
        user_answer = input("Type an answer:")
        if user_answer == "C".casefold():
            correct_answers += 1
            print("Correct\n")
            continue
        else:
            wrong_answers += 1
            print("Wrong answer.\n")
    elif current_question == "Question: What is the color of the sky?":
        print("A: Red, B: Black, C: Orange", "D: Blue")
        user_answer = input("Type an answer:")
        if user_answer == "D".casefold():
            correct_answers += 1
            print("Correct\n")
            continue
        else:
            wrong_answers += 1
            print("Wrong answer.\n")

if wrong_answers >= 2:
    print(f"You Lost! You have {wrong_answers} wrong answers.")
else:
    print(f"Congratulations! You won! You have {correct_answers} correct answers.")
