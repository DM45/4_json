import json
import os


def load_json_data(filepath):
    if not os.path.exists(filepath):
        return None
    with open(filepath, 'r') as file_handler:
        return json.load(file_handler)


def pretty_print_json(json_data):
    return json.dumps(json_data, sort_keys=True, indent=4)


if __name__ == '__main__':
    _filepath = input('Filepath: ')
    _json_data = load_json_data(_filepath)
    print('Pretty printed view of json file')
    print(pretty_print_json(_json_data))
