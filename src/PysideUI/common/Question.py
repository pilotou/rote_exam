class Question:
    def __init__(self, id,q_id, question, answer, choice, choice_num, q_type, difficulty,source,
                 recent_answer="",wrong_times=0,right_times=0,last_answer_date="",last_wrong_answer=""):

        self.id = id
        self.q_id = q_id
        self.question = question
        self.answer = answer
        self.choice = choice
        self.choice_num = choice_num
        self.type = q_type
        self.difficulty = difficulty
        self.source = source
        self.recent_answer = recent_answer
        self.wrong_times = wrong_times
        self.right_times = right_times
        self.last_answer_date = last_answer_date
        self.last_wrong_answer = last_wrong_answer

    def show(self):
        return f"{self.q_id}.{self.question}\n{self.choice}\n"

    def check(self, ans: str):
        return ans.upper() == self.answer.upper()

    def note_question(self):
        return f"{self.show()}正确答案：{self.answer}\n你的答案:{self.recent_answer}\n"