import random
from data.test.test_questions import brother


class BrotherTestUser:
    def __init__(self, level=0, current_question=1, current_question_answer=-1, correct_answers=0):
        self.level = level
        self.current_question = current_question
        self.current_question_answer = current_question_answer
        self.correct_answers = correct_answers
        self.time_to_answer = 20
        self.question = {'options': [], 'answer': -1}
        self.poll_id = -1

    @staticmethod
    def create_option():
        first_num = random.randint(0, 9)
        second_num = random.randint(-9, 9)
        return f'{first_num}+{second_num}' if second_num >= 0 else f'{first_num}{second_num}'

    def create_question(self):
        options = []
        answer = -1
        for i in range(4):
            option = self.create_option()

            if option in brother and answer == -1:
                answer = i
            elif option in brother and answer > -1:
                while option in brother:
                    option = self.create_option()
            elif option in options:
                while option in options:
                    option = self.create_option()
            options.append(option)

        if answer == -1:
            answer = 4

        options.append('Среди прмеров нет такого')
        self.question['options'] = options
        self.question['answer'] = answer
