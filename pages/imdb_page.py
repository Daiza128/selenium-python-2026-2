import re
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from .base_page import BasePage

class ImdbPage(BasePage):
    SEARCH_FIELD = (By.ID, 'suggestion-search')
    FIRST_RESULT = (By.CSS_SELECTOR, "section[data-testid='find-results-section-title'] a.ipc-title-link-wrapper")
    MOVIE_TITLE = (By.TAG_NAME, 'h1')
    RATING = (By.CSS_SELECTOR, "[data-testid='hero-rating-bar__aggregate-rating__score']")

    def search(self, movie_name):
        self.enter_text(self.SEARCH_FIELD, movie_name + Keys.ENTER)

    def open_first_result(self):
        self.click(self.FIRST_RESULT)

    def get_movie_title(self):
        return self.find_element(self.MOVIE_TITLE).text

    def get_rating(self):
        # El texto viene como "8.8/10" o "8,8/10"; se toma el primer número
        rating_text = self.find_element(self.RATING).text
        return float(re.search(r'\d+(?:[.,]\d+)?', rating_text).group().replace(',', '.'))
