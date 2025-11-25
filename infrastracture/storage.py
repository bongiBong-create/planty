import json
from pathlib import Path

def init_path(json_name="plants.json"):
    return Path(__file__).parent / json_name

def init_storage(path):
    if not path.exists():
        with open(path, "w", encoding="utf-8") as f:
            json.dump([], f)

def get_data(path):
    with open(path, "r", encoding="utf-8") as f:
        return json.load(f)

def save_data(path, plants):
    with open(path, "w", encoding="utf-8") as f:
        json.dump(plants, f, ensure_ascii=False)