from question_model import Question
from data import question_data
from quiz_byte import QuizByte
import pyfiglet
question_bank=list()
logo=pyfiglet.figlet_format("Quiz Byte")
for question in question_data:
    question_bank.append(Question(question['text'],question['answer']))
quiz=QuizByte(question_bank)
print(logo)
while quiz.still_question_left():
    quiz.next_question()
    quiz.check_answer()
    print("\n"*20)
    print(logo)
    print(f"Your current score is {quiz.point}/{quiz.question_number + 1}")
print("\n"*20)
print(logo)
print(f"\nYour final score is {quiz.point}/{quiz.question_number+1}")
