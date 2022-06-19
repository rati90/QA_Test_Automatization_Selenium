import pytest

from pages.about_page import AboutPage
from utility.datautils import ReadJSON


json_file = ReadJSON()


@pytest.mark.usefixtures('browser')
class TestAbout:
    def test_about_page(self):
        self.about_page = AboutPage()
        self.about_page.browser.get(json_file.get_base_url())
        assert self.about_page.get_status(AboutPage.store_page_unique) is True, 'Is not on the Main page'

        self.about_page.do_click(AboutPage.store_search_about_page)
        assert self.about_page.get_status(AboutPage.about_page_unique) is True, 'About page is not opened'

        gamers_online = self.about_page.get_numbers_from_text(AboutPage.gamers_online)
        gamers_in_game = self.about_page.get_numbers_from_text(AboutPage.gamers_in_game)
        assert gamers_online > gamers_in_game, 'Data is not correct'

        self.about_page.do_click(AboutPage.store)
        assert self.about_page.get_status(AboutPage.store_page_unique) is True, 'Store page is not opened'
