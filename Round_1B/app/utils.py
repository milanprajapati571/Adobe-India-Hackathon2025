import json

def read_input_json(path):
    with open(path, "r", encoding="utf-8") as f:
        return json.load(f)
