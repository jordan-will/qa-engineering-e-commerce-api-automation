import json 
from pathlib import Path

def load_json(file_path: str | Path):
    path = Path(file_path)

    with path.open("r", encoding="utf-8") as file:
        return json.load(file)

def load_model(file_path: str | Path, model_class):
    data = load_json(file_path)
    return [
        model_class(**item)
        for item in data
    ]