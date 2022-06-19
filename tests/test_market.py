from pages.market_page import MarketPage

from utility.datautils import ReadJSON

json_file = ReadJSON()


class TestMarket:
    def test_market(self):
        self.market = MarketPage()
        self.market.browser.get(json_file.get_base_url())
        assert self.market.get_status(MarketPage.store_page_unique) is True, 'Is not on the Main page'

        self.market.hover_mouse(MarketPage.store_community)
        self.market.wait_element(MarketPage.store_search_market_page)
        self.market.do_click(MarketPage.store_search_market_page)
        assert self.market.get_status(MarketPage.marker_page_unique) is True, 'Is not on the Market Page'

        self.market.do_click(MarketPage.advanced_option)
        assert self.market.get_status(MarketPage.advanced_window_unique) is True, "Advanced window is not opened"

        self.market.do_click(MarketPage.games_selector)
        self.market.do_click(MarketPage.dota2)
        self.market.selector_with_text(MarketPage.hero_selector, 'Lifestealer')
        self.market.do_click(MarketPage.rarity_immortal)
        self.market.send_text(MarketPage.search_field, 'golden')
        self.market.do_enter(MarketPage.search_field)

        search_text = self.market.get_text(MarketPage.search_result)
        assert json_file.get_testscase3()['Games'] in search_text, f"{json_file.get_testscase3()['Games'] } is not searched"
        assert json_file.get_testscase3()['Hero'] in search_text, f"{json_file.get_testscase3()['Hero']} is not searched"
        assert json_file.get_testscase3()['Rarity'] in search_text, f"{json_file.get_testscase3()['Rarity']} is not searched"
        assert json_file.get_testscase3()['Search'] in search_text, f"{json_file.get_testscase3()['Search']} is not searched"

        search_row = self.market.get_all_elements(MarketPage.search_result_row)
        selected_item_titles = self.market.get_text_from_elements(search_row)

        for title in selected_item_titles[:5]:
            assert 'Golden' in title, 'text does not include Golden'

        self.market.do_click(MarketPage.remove_search_path(self, '"golden"'))
        self.market.do_click(MarketPage.remove_search_path(self, 'Dota 2'))
        self.market.browser.refresh()

        search_row = self.market.get_all_elements(MarketPage.search_result_row)
        selected_item_titles = self.market.get_text_from_elements(search_row)
        item_out_name = selected_item_titles[0]

        search_text2 = self.market.get_text(MarketPage.search_result)
        assert json_file.get_testscase3()['Search'] not in search_text2, f"{json_file.get_testscase3()['Search']} is not removed"
        assert json_file.get_testscase3()['Games'] not in search_text2, f"{json_file.get_testscase3()['Games'] } is not removed"

        self.market.do_click(MarketPage.search_result_first)
        assert self.market.get_status(MarketPage.first_result_unique) is True, 'Items page is not opened'

        item_game_name = self.market.get_text(MarketPage.item_game_name)
        item_used = self.market.get_text(MarketPage.item_used_by)
        item_in_name = self.market.get_text(MarketPage.item_name)
        item_rarity = self.market.get_text(MarketPage.item_rarity)
        assert item_game_name == json_file.get_testscase3()['Games'], 'Item name is not as selected'
        assert json_file.get_testscase3()['Hero'] in item_used, 'Item used by is not as selected'
        assert item_out_name in item_in_name, 'Item names are not the same'
        assert json_file.get_testscase3()['Rarity'] in item_rarity, 'Item rarity is not as selected'
