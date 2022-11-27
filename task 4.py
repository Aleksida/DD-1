import json

INPUT_FILE = "input.csv"


def csv_to_list_dict(filename, delimiter = ',') -> list[dict]:
    with open(filename, "r") as f:
        headers = f.readline()[:-1].split(delimiter)
        rows = [i[:-1].split(delimiter) for i in f.readlines()]
    return [dict(zip(headers,i)) for i in rows]



print(json.dumps(csv_to_list_dict(INPUT_FILE), indent=4))
