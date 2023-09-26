import random
import csv

# def chon_phuong_an(prompt):
#     while True:
#         answer = input(prompt).upper()
#         if answer in ["A", "B", "C", "D"] or answer in ["0", "1", "2"]:
#             return answer
#         else:
#             continue
# # Khai báo biến để kiểm tra việc sử dụng quyền trợ giúp
# used_50_50 = False
# used_audience = False
#
# def help_50_50():
#     global used_50_50
#     if not used_50_50:
#         print("Tro giup 50-50")
#         used_50_50 = True
#     else:
#         print("Bạn đã sử dụng quyền trợ giúp 50-50 rồi, không thể sử dụng lại.")
#
# def help_audience():
#     global used_audience
#     if not used_audience:
#         print("Tro giup audience")
#         used_audience = True
#     else:
#         print("Bạn đã sử dụng quyền trợ giúp Audience rồi, không thể sử dụng lại.")
#
# def main():
#     global used_50_50
#     global used_audience
#     if used_50_50:
#         print("Bạn không thể sử dụng quyền trợ giúp 50-50 nữa.")
#     else:
#         ask_help = input("Ban co muon su dung quyen tro giup (1, 2, 3): ")
#         if ask_help == "1":
#             help_50_50()
#         else:
#             used_50_50 = False  # Đặt lại trạng thái quyền trợ giúp 50-50
#     if used_audience:
#         print("Ban khong the su dung quyen tro giup Audience.")
#     else:
#         ask_help = input("Ban co muon su dung quyen tro giup (1, 2, 3): ")
#         if ask_help == "2":
#             help_audience()
#         else:
#             used_audience = False
#         main()
#
# if __name__ == "__main__":
#     main()
#
#
#
#
#
# # def help_50_50():
# #     print("tro giup 50-50")
# # def help_audience():
# #     print("Tro giup audience")
# #
# # def main():
# #     ask_help = chon_phuong_an("Ban co muon su dung quyen tro giup (1, 2, 3): ")
# #     if ask_help == "1":
# #         help_50_50()
# #         main()
# #     if ask_help == "2":
# #         help_audience()
# #         main()
# #     else:
# #         ask_help = False
# # main()
# import random
# import csv
#
# def question_for_quiz(all_questions):
#     random_questions = random.sample(all_questions, 15)
#     return random_questions
# # # 15 Question
# def random_question(questions):
#     print(questions)
#     # for i in range(0, 15):
#     #     ran_question = random.choice(questions)
#     #     print(ran_question)
#
# def set_question():
#     questions = []
#     with open("Q&A.csv", encoding='utf-8') as data_file:
#         reader = csv.DictReader(data_file)
#         for row in reader:
#             question = {
#                 "question": row["Câu hỏi"],
#                 "answers": [row["Đáp án A"], row["Đáp án B"], row["Đáp án C"], row["Đáp án D"]],
#                 "correct": row["Đáp án chính xác"]
#             }
#             questions.append(question)
#     return questions
#
#
# def main():
#     questions = set_question()
#     questions_15 = question_for_quiz(questions)
#     random_question(questions_15)
#
# # # Chuong trinh chinh
# main()


# questions = []
# with open("Q&A.csv", encoding='utf-8') as data_file:
#     reader = csv.DictReader(data_file)
#     for row in reader:
#         question = {
#             "question": row["Câu hỏi"],
#             "answers": [row["Đáp án A"], row["Đáp án B"], row["Đáp án C"], row["Đáp án D"]],
#             "correct": row["Đáp án chính xác"]
#         }
#         questions.append(question)
#         print(question)


# question = {
#     "answers": ["A", "B", "C", "D"],
#     "correct": "D"
# }
#
# correct_index = question["answers"].index(question["correct"])
# print(correct_index)  # Kết quả sẽ là 1, vì "B" nằm ở chỉ mục thứ 1 trong danh sách câu trả lời.

# a = random.random()
# print(a)

# a = random.uniform(0.5, 0.9)
# print(a*100)

correct_answer = "A"  # Thay thế bằng câu trả lời đúng thực tế
all_answers = ["A", "B", "C", "D"]  # Thay thế bằng danh sách tất cả câu trả lời

# Tính tỷ lệ đúng dựa trên tỷ lệ sai
total_percentage = 100  # Tổng tỷ lệ (100%)
incorrect_percentage = random.uniform(10, 40)  # Tỷ lệ sai ngẫu nhiên từ 10% đến 40%
correct_percentage = total_percentage - incorrect_percentage  # Tỷ lệ đúng

# Tạo một từ điển để lưu trữ tỷ lệ đoán của khán giả
audience_guess = {}

# Gán tỷ lệ đúng và sai cho từng câu trả lời
for choice in all_answers:
    if choice == correct_answer:
        audience_guess[choice] = correct_percentage / 100
    else:
        audience_guess[choice] = incorrect_percentage / (len(all_answers) - 1) / 100

print(audience_guess)
