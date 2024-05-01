from data import Urls
from pages.questions_page import QuestionsPage
import pytest

class TestQuestionAnswer:

    @pytest.mark.parametrize("question_number", [1, 2, 3, 4, 5, 6, 7, 8])
    def test_question_answer(self, driver, question_number):
        questions_page = QuestionsPage(driver)
        questions_page.open_url(Urls.SCOOTER)
        questions_page.click_question_button(question_number)

        answer_element = questions_page.get_answer(question_number)
        assert answer_element.is_displayed()