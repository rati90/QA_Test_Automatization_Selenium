from selenium.webdriver.common.by import By

from pages.base_page import BasePage


class AboutPage(BasePage):
    store_page_unique = (By.XPATH, "//div[@id='store_controls']")
    about_page_unique = (By.XPATH, "//div[@id='about_header_area']")
    store_search_about_page = (By.XPATH, "//a[@class='menuitem' and contains(text(), 'ABOUT')]")
    search_about_page = (By.XPATH, "//a[@class='menuitem' and contains(text(), 'ABOUT')]")
    gamers_online = (By.XPATH, "//div[@class='online_stat_label gamers_online']//parent::div")
    gamers_in_game = (By.XPATH, "//div[@class='online_stat_label gamers_in_game']//parent::div")
    store = (By.XPATH, "//a[@class='menuitem supernav' and contains(text(), 'STORE')]")

    def __init__(self):
        super().__init__()
