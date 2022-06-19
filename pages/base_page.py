from selenium.webdriver import ActionChains
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys

from utility.datautils import ReadJSON
from utility.utils import get_only_numbers
from utility.webdriver import WebDriver

json_file = ReadJSON()

class BasePage:

    def __init__(self):
        self.browser = WebDriver().driver
        self.wait = WebDriverWait(self.browser, json_file.get_wait_time())

    def do_click(self, by_locator):
        self.wait.until(EC.visibility_of_element_located(by_locator)).click()

    def get_title(self, title):
        self.wait.until(EC.title_is(title))
        return self.browser.title

    def get_text(self, by_locator):
        return self.wait.until(EC.visibility_of_element_located(by_locator)).text

    def get_numbers_from_text(self, by_locator):
        text = self.wait.until(EC.visibility_of_element_located(by_locator)).text

        return get_only_numbers(text)

    def hover_mouse(self, by_locator):
        element = self.wait.until(EC.visibility_of_element_located(by_locator))
        ActionChains(self.browser).move_to_element(element).perform()

    def wait_element(self, by_locator):
        self.wait.until(EC.visibility_of_element_located(by_locator))

    def get_current_url(self):
        return self.browser.current_url

    def get_status(self, by_locator):
        if self.wait.until(EC.visibility_of_element_located(by_locator)):
            return True

    def selector_with_text(self, by_locator, text):
        element = self.wait.until(EC.visibility_of_element_located(by_locator))
        selector = Select(element)
        selector.select_by_visible_text(text)

    def send_text(self, by_locator, text):
        self.wait.until(EC.visibility_of_element_located(by_locator)).send_keys(text)

    def do_enter(self, by_locator):
        self.wait.until(EC.visibility_of_element_located(by_locator)).send_keys(Keys.ENTER)

    def get_current_list(self, by_locator):
        search = self.wait.until(EC.presence_of_all_elements_located(by_locator))
        games = [i for i in search if len(i.text) > 0]
        return games

    def get_element(self, by_locator):
        return self.wait.until(EC.visibility_of_element_located(by_locator))

    def get_all_elements(self, by_locator):
        return self.wait.until(EC.visibility_of_all_elements_located(by_locator))


    def get_text_from_elements(self, element):
        text = [i.text for i in element]
        return text

    def get_element_is_visable(self, by_locator):
        return self.wait.until(EC.invisibility_of_element_located(by_locator))

