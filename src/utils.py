import json
from pathlib import Path


def get_operations(path: str) -> list:
    """
    Читает JSON-файл с транзакциями и возвращает список словарей.
    Если файл не найден, пустой или содержит не список — возвращается пустой список.
    """
    try:
        with open(path, "r", encoding="utf-8") as f:
            data = json.load(f)
    except (FileNotFoundError, json.decoder.JSONDecodeError):
        return []

    if not isinstance(data, list):
        return []

    return data
