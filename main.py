import csv
import pandas as pd
import random
import sys

# # Repeat answer is you respond incorrect value
def ask_yes_no(prompt):
    while True:
        answer = input(prompt)
        if answer == "Yes" or answer == "Y" or answer == "y" or answer == "YES" or answer == "yes":
            return True
        elif answer == "No" or answer == "N" or answer == "n" or answer == "NO" or answer == "no":
            return False
            break
        else:
            continue
# # Select A, B, C, D
def chon_dap_an(prompt):
    while True:
        answer = input(prompt).upper()
        if answer in ["A", "B", "C", "D"]:
            return answer
        else:
            continue
# # Select method help:
# #               "0": Continue game
# #               "1": Help 50_50
# #               "2": Help Audience
def chon_phuong_an(prompt):
    while True:
        answer = input(prompt).upper()
        if answer in ["0", "1", "2"]:
            return answer
        else:
            continue


# # Random 15/30 questions
def question_for_quiz(all_questions):
    random_questions = random.sample(all_questions, 15)
    return random_questions
# # 15 Question
def random_question(questions):
    score = 0
    question = question_for_quiz(questions)
    for i, ran_question in enumerate(question,1):
        print(f"\nCâu hỏi số {i}:")
        if ask_question(ran_question):
            print("Chúc mừng, bạn đã trả lời đúng!\n")
            score += 1
            print("Score of you: ", score)
        else:
            score = 0
            print("Rất tiếc, bạn đã trả lời sai.\n")
            print("Đáp chính xác của câu hỏi: ", ran_question["correct"])
            print("Score of you: ", score)
            print("Thank you that you go this program")
            ask_play_game = play_again()
            main(ask_play_game)
        if i == 15:
            print("Chuc mung! Ban la trieu phu !")
            print("You receive a bonus of " + str(score) + " million VND" )
            main(play_again())
        if i > 1:
            ask_continue = ask_yes_no("Ban co muon tiep tuc game ?(Yes/No): ")
            if ask_continue == True:
                continue
            else:
                print("You receive a bonus of: ", score)
                print("Thank you that you go this program")
                ask_play_game = play_again()
                main(ask_play_game)

# # Respond answer of you
def ask_question(question):
    global used_helps
    print(question["question"])
    for j, answer in enumerate(question["answers"]):
        print(f"{chr(65 + j)}. {answer}")
    # Select Help you
    if len(used_helps) < 2:
        choice_help_you(question)
    else:
        print("Ban da het quyen su dung tro giup")
    user_answer = chon_dap_an("Câu trả lời của bạn là, hãy chọn đáp án (A/B/C/D): ")
    if user_answer == chr(65 + question["answers"].index(question["correct"])):
        return True
    else:
        return False

# # Set up questions from CSV file
def set_question():
    questions = []
    try:
        with open("Q&A.csv", encoding='utf-8') as data_file:
            reader = csv.DictReader(data_file)
            for row in reader:
                question = {
                    "question": row["Câu hỏi"],
                    "answers": [row["Đáp án A"], row["Đáp án B"], row["Đáp án C"], row["Đáp án D"]],
                    "correct": row["Đáp án chính xác"]
                }
                questions.append(question)
    except Exception as e:
        print(f"Error reading the CSV file: {str(e)}")
    return questions

# # Choice "1" - Help 50/50
def help_50_50(question):
    all_answers = []
    for j, answer in enumerate(question["answers"]):
        all_answers.append(f"{chr(65 + j)}. {answer}")
    correct_answer = question["correct"]
    correct_answer = chr(65 + question["answers"].index(question["correct"])) + ". " + correct_answer
    # Select incorrect answers
    incorrect_answer = []
    for answer in all_answers:
        if answer != correct_answer:
            incorrect_answer.append(answer)
    # Select random 1 in 3 of incorrect
    incorrect_1_answer = random.choice(incorrect_answer)
    incorrect_answer.remove(incorrect_1_answer)
    # Appear two incorrect is empty
    for m in incorrect_answer:
        for n in range(len(all_answers)):
            if m in all_answers[n]:
                m = chr(65 + n) + ". ____________________"
                all_answers[n] = m
            else:
                continue
    return all_answers

# # Choice "2" - Audience
def help_audience(question):
    all_answers = []
    for j, answer in enumerate(question["answers"]):
        all_answers.append(f"{chr(65 + j)}. {answer}")
    correct_answer = question["correct"]
    correct_answer = chr(65 + question["answers"].index(question["correct"])) + ". " + correct_answer
    # Create rates of audience
    audience_guess = {}
    rate_incorrect = 0
    for choice in all_answers:
        if choice == correct_answer:
            audience_guess[choice] = random.uniform(0.5,0.9)
            rate_incorrect = 1 - audience_guess[choice]
        else:
            audience_guess[choice] = random.uniform(0.1, rate_incorrect)
        rate_incorrect = rate_incorrect
    # Prediction of audience
    print("Dự đoán của khán giả:")
    # Print export prediction of audience
    for choice, likelihood in audience_guess.items():
        print(f"{choice} \n Rate of Audiences is -> {likelihood * 100}%")

# # Show menu
def show_menu():
    print("+++ _________________________+++")
    print(" ----Hay chon quyen tro giup----")
    print("--------------------------------")
    print("| Option 0: Continue games      |")
    print("| Option 1: Help 50-50          |")
    print("| Option 2: Help from Audience  |")
    print("--------------------------------")

# # Choice help you
used_helps = []
def choice_help_you(question):
    global used_helps
    ask_help = ask_yes_no("Do you use help ?(Yes/no) ")
    if ask_help == True:
        show_menu()
        sel_pick = chon_phuong_an("Enter number which you want: (0, 1, 2): ")
        if sel_pick == "0" and "0" not in used_helps:
            ask_help = False
        if sel_pick == "1" and "1" not in used_helps:
            answer = help_50_50(question)
            print("Repeat question: " + question["question"])
            for ans in answer:
                print(ans)
            used_helps.append("1")
            print("Ban da su dung quyen tro giup 50-50")
        elif sel_pick == "1" and "1" in used_helps:
            print("Ban khong the su dung quyen tro giup 50-50.")
            sel_pick = chon_phuong_an("Enter number again which you want: (0, _, 2): ")
        if sel_pick == "2" and "2" not in used_helps:
            help_audience(question)
            used_helps.append("2")
            print("Ban da su dung quyen tro giup Audience")
        elif sel_pick == "2" and "2" in used_helps:
            print("Ban khong the su dung quyen tro giup Audience.")
            sel_pick = chon_phuong_an("Enter number again which you want: (0, _, 1): ")

# # Play again
def play_again():
    global used_helps
    # Reset use helps
    used_helps = []
    ask_start = ask_yes_no("Ban co muon bat dau lai game ?(Yes/No): ")
    return  ask_start

# # Function chua cac chuong trinh con
def main(ask_start):
    global used_helps
    # Reset use helps
    used_helps = []
    if ask_start == True:
        print("Welcome, Thank you for your presence")
        print("***--You are the lucky one this evening--***")
        questions = set_question()
        questions_15 = question_for_quiz(questions)
        random_question(questions_15)
    else:
        sys.exit("Thank you that you go this program")

# # Chuong trinh chinh
ask_start = ask_yes_no("Ban co muon bat dau game ?(Yes/No): ")
main(ask_start)

