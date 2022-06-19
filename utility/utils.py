import json


def get_only_numbers(text):
    numbers = ''.join(filter(str.isdigit, text.strip()))
    return int(numbers)


def read_json(directory):
    with open(directory, 'r') as json_file:
        json_data = json.load(json_file)
        return json_data
