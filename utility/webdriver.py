from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager


class WebDriver:
    class __WebDriver:
        def __init__(self):
            options = self.get_options()

            self.driver = webdriver.Chrome(options=options,
                                           service=Service(ChromeDriverManager().install()))



        @staticmethod
        def get_options():
            options = webdriver.ChromeOptions()
            options.add_argument('--incognito')
            options.add_argument("start-maximized")
            options.add_experimental_option("excludeSwitches", ["enable-logging"])

            return options

    driver = None

    def __init__(self):
        if not self.driver:
            WebDriver.driver = WebDriver.__WebDriver().driver
    #
    # def driver_quit(self):
    #     if self.driver:
    #         self.driver.quit()
    #         self.driver = None