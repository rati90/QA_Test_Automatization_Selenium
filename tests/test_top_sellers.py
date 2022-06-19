from pages.top_sellers import TopSellers
from utility.datautils import ReadJSON

json_file = ReadJSON()


class TestSellers:
    def test_top_sellers(self):

        self.top_sellers = TopSellers()
        self.top_sellers.browser.get(json_file.get_base_url())
        assert self.top_sellers.get_status(TopSellers.store_main_page_unique) is True, 'Is not on the Main page'

        self.top_sellers.hover_mouse(TopSellers.store_new_noteworthy)
        self.top_sellers.do_click(TopSellers.store_top_sellers)
        assert self.top_sellers.get_status(TopSellers.top_sellers_unique) is True, 'Is not on the top_sellers page'
        self.top_sellers.do_click(TopSellers.narrow_by_players)
        self.top_sellers.do_click(TopSellers.action_checkbox)
        self.top_sellers.do_click(TopSellers.lan_coop_checkbox)
        self.top_sellers.do_click(TopSellers.steamsos_linux_checkbox)

        assert self.top_sellers.get_status(TopSellers.action_checkbox_checked) is True, 'Action is not checked'
        #can not manage to find the Lan C00 checked Xpath
        assert self.top_sellers.get_status(TopSellers.steamsos_linux_checkbox_checked) is True, 'SteamsOs + linux is ' \
                                                                                                'not checked '

        self.top_sellers.get_element_is_visable(TopSellers.opasity_element)
        search_result = self.top_sellers.get_numbers_from_text(TopSellers.result_match)
        selected_games = self.top_sellers.get_current_list(TopSellers.list_of_games)
        assert search_result == len(selected_games), 'It may not be same, steam have a bug here.' \
                                                     'search number is not same as displayed'


        title = self.top_sellers.get_current_list(TopSellers.list_of_titles)
        release_date = self.top_sellers.get_current_list(TopSellers.list_of_dates)
        prices = self.top_sellers.get_current_list(TopSellers.list_of_prices)
        out_title = title[0].text
        out_release_date = release_date[0].text
        out_price = prices[0].text

        self.top_sellers.do_click(TopSellers.list_of_games)
        assert self.top_sellers.get_status(TopSellers.game_page_unique) is True, 'Is not on the game page'

        in_title = self.top_sellers.get_text(TopSellers.opened_title)
        in_release_date = self.top_sellers.get_text(TopSellers.opened_date)
        in_price = self.top_sellers.get_text(TopSellers.opened_price)

        assert out_title == in_title, 'titles are not the same'
        assert out_release_date == in_release_date, 'release dates are not the same'
        assert out_price == in_price[:-4], 'prices are not the same'




