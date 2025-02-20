class QuizByte:
    def __init__(self,q_list):
        self.question_number=-1
        self.question_list=q_list
        self.point=0
        self.answer=""
    def next_question(self):
        self.question_number+=1
        current_question=self.question_list[self.question_number]
        self.answer=input(f"Q.{self.question_number+1} {current_question.text}. (True/False)?: ").capitalize()
    def check_answer(self):
        if self.answer == self.question_list[self.question_number].answer:
            print("You got it right!")
            self.point+=1
        else:
            print("That's wrong!")
    def still_question_left(self):
        if self.question_number<len(self.question_list)-1:
            return True
        else:
            return False
