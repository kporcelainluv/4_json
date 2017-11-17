import json
import sys

def convert_file_to_pretty(data_from_file):
    prettyfied_file = json.dumps(json.loads(data_from_file), indent=5, sort_keys=True, ensure_ascii=False)
    return prettyfied_file


if __name__ == '__main__':
    if len(sys.argv) > 1:
        with open(sys.argv[1], "r") as input_file:
            print(convert_file_to_pretty(input_file.read()))
