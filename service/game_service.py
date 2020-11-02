from constants.constants import UserKeys, QuestionKeys
from question_set import question_sets
class GameService:
    def check_answer(self, question_dict):
        # {'question_id': {
        #   'question_id': 'blah',
        #   'question_name': 'blah',
        #   'question_answer': 'blah'
        # }}
        question_id = question_dict.get(QuestionKeys.QUESTION_ID)
        question_set = question_sets.get(question_id)
        user_answer = question_dict.get(QuestionKeys.QUESTION_ANSWER)
        correct_answer = question_set.get(QuestionKeys.QUESTION_ANSWER)
        return user_answer == correct_answer