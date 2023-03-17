from data.test.brother_test_user import BrotherTestUser
from data.test.theory_test_user import TheoryTestUser

brother_test_data = {}
theory_test_data = {}


def check_brother_user(_id):
    if _id not in brother_test_data:
        brother_test_data[_id] = BrotherTestUser()
        user: BrotherTestUser = brother_test_data.get(_id)
    else:
        user: BrotherTestUser = brother_test_data.get(_id)
        user.current_question = 1
        user.current_question_answer = -1
        user.correct_answers = 0
        user.time_to_answer = 20 - user.level * 5
    return user


def get_brother_user(user_id: int):
    user: BrotherTestUser = brother_test_data.get(user_id)
    return user


def check_theory_user(_id):
    if _id not in theory_test_data:
        theory_test_data[_id] = TheoryTestUser()
    user = theory_test_data.get(_id)
    return user


def get_theory_user(user_id: int):
    user: TheoryTestUser = theory_test_data.get(user_id)
    return user
