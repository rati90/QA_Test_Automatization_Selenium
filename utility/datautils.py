
from utility.utils import read_json

config_data = r'.\config\configdata.json'
test_data = r'.\testdata\testdata.json'


class ReadJSON:
    def __init__(self):
        self.config_data = read_json(config_data)
        self.test_data = read_json(test_data)

    def get_base_url(self):
        return self.config_data['baseurl']

    def get_wait_time(self):
        return self.config_data['wait_time']

    def get_checkbox_data(self):
        return self.test_data['checkbox']

    def get_testscase3(self):
        return self.test_data['testcase3']


