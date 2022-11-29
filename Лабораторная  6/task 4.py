import json
from typing import List

INPUT_FILE = "input.csv"


def csv_to_list_dict(filename, delimiter=',', newline='\n') -> List[dict]:
    with open(filename) as f:
        data_list = []
        is_header = True
        for row in f:
            list_rows = row.rstrip().split(newline)
            for line in list_rows:
                if is_header:
                    headers = line.split(delimiter)
                    is_header = False
                    continue
                data_list.append(dict(zip(headers, line.split(delimiter))))
    return data_list


print(json.dumps(csv_to_list_dict(INPUT_FILE), indent=4))