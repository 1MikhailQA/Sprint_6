from locators.questions_locators import Questions
from pages.base_page import BasePage

class QuestionsPage(BasePage):

    def click_question_button(self, question_number):
        question_locator = getattr(Questions, f"QUESTION_{question_number}_LOCATOR")
        question_button = self.wait_and_find_element(*question_locator)
        self.driver.execute_script("arguments[0].scrollIntoView();", question_button)
        self.scroll_down()
        self.click_element_with_retry(question_button)

    def get_answer(self, question_number):
        answer_locator = getattr(Questions, f"ANSWER_{question_number}_LOCATOR")
        return self.wait_and_find_element(*answer_locator)

