import json
import sys


def load_data():
    with open(filename, "r") as input_file:
        json_file = input_file.read().strip()
    return json_file


def pretty_print_json(data_from_file):
    load_data_from_file = json.loads(data_from_file)
    json_format_file = json.dumps(load_data_from_file, indent=5, sort_keys=True, ensure_ascii=False)
    return json_format_file


if __name__ == '__main__':
    if len(sys.argv) > 1:
        filename = sys.argv[1]
        print(pretty_print_json(load_data()))
