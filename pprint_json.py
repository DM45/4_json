import json
import os


def load_json_data(filepath):
    if not os.path.exists(filepath):
        return None
    with open(filepath, 'r') as file_handler:
        return json.load(file_handler)


def pretty_print_json(data):
    return json.dumps(data, sort_keys=True, indent=4)


if __name__ == '__main__':
    _filepath = input(str)
    _data = load_json_data(_filepath)
    print(pretty_print_json(_data))
