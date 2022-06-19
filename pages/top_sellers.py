from selenium.webdriver.common.by import By

from pages.base_page import BasePage
from utility.datautils import ReadJSON

json_file = ReadJSON()


class TopSellers(BasePage):
    top_sellers_unique = (By.XPATH, "//div[@id='search_results_filtered_warning_persistent']")
    store_main_page_unique = (By.XPATH, "//div[@id='store_controls']")
    store_new_noteworthy = (By.XPATH, "//div[@id='noteworthy_tab']")
    store_top_sellers = (By.XPATH, "//a[@class='popup_menu_item' and contains(text(), 'Top Sellers')]")

    action_checkbox = (By.XPATH, f"//span[normalize-space()='{json_file.get_checkbox_data()[0]}']")
    action_checkbox_checked = (By.XPATH, f"//span[@class='label'][normalize-space()='{json_file.get_checkbox_data()[0]}']")

    narrow_by_players = (By.XPATH, "//div[contains(text(),'Narrow by number of players')]")
    lan_coop_checkbox = (By.XPATH, f"//span[contains(text(),'{json_file.get_checkbox_data()[1]}')]")

    steamsos_linux_checkbox = (By.XPATH, f"//span[contains(text(),'{json_file.get_checkbox_data()[2]}')]")
    steamsos_linux_checkbox_checked = (By.XPATH, "//div[@data-value='linux']")

    opasity_element = (By.XPATH, "//div[contains(@style, 'opacity')]")
    result_match = (By.XPATH, "//div[@class='search_results_count']")

    list_of_games = (By.XPATH, "//div[@class='responsive_search_name_combined']")
    list_of_titles = (By.XPATH, "//span[@class='title']")
    list_of_dates = (By.XPATH, "//div[@class='col search_released responsive_secondrow']")
    list_of_prices = (By.XPATH, "//div[@class='col search_price_discount_combined responsive_secondrow']")

    game_page_unique = (By.XPATH, "//div[@id='gameHeaderImageCtn']")

    opened_title = (By.XPATH, "//div[@id='appHubAppName']")
    opened_date = (By.XPATH, "//div[@class='date']")
    opened_price = (By.XPATH, "//div[@class='game_purchase_price price']")

    def __init__(self):
        super().__init__()

