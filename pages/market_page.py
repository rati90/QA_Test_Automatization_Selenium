from selenium.webdriver.common.by import By

from pages.base_page import BasePage


class MarketPage(BasePage):
    store_page_unique = (By.XPATH, "//div[@id='store_controls']")
    marker_page_unique = (By.XPATH, "//a[@id='tabMyListings']")
    advanced_option = (By.XPATH, "//div[@id='market_search_advanced_show']")

    store_community = (By.XPATH, "//a[@class='menuitem supernav' and contains(text(), 'COMMUNITY')]")
    store_search_market_page = (By.XPATH, "//div[@class='supernav_content']//a[@class='submenuitem'][normalize-space("
                                          ")='Market']")

    advanced_window_unique = (By.XPATH, "//div[@id='market_advancedsearch_dialog']")
    games_selector = (By.XPATH, "//div[@id='market_advancedsearch_appselect']")
    dota2 = (By.XPATH, "//div[@id='app_option_570']")
    hero_selector = (By.XPATH, "//select[@name='category_570_Hero[]']")
    rarity_immortal = (By.XPATH, "//input[@id='tag_570_Rarity_Rarity_Immortal']")
    search_field = (By.XPATH, "//input[@id='advancedSearchBox']")

    search_result = (By.XPATH, "//div[@class='market_search_results_header']//div")
    search_result_row = (By.XPATH, "//span[@class='market_listing_item_name']")

    search_result_first = (By.XPATH, "//div[@id='result_0']//div[@class='market_listing_item_name_block']")
    first_result_unique = (By.XPATH, "//div[@id='market_buyorder_info']")

    item_game_name = (By.XPATH, "//div[@id='largeiteminfo_game_name']")
    item_used_by = (By.XPATH, "//div[@id='largeiteminfo_item_descriptors']//child::div")
    item_name = (By.XPATH, "//div[@id='largeiteminfo_content']//div[@class='item_desc_description']")
    item_rarity = (By.XPATH, "//div[@id='largeiteminfo_item_type']")

    def __init__(self):
        super().__init__()

    def remove_search_path(self, text):
        path = (By.XPATH, f"//a[normalize-space()= '{text}']")

        return path
