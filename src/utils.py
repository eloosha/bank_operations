import json
import logging
from pathlib import Path
import pandas as pd

logger = logging.getLogger("utils")
logger.setLevel(logging.DEBUG)
file_handler = logging.FileHandler("logs/utils.log", mode="w", encoding="utf-8")
file_formatter = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s")
file_handler.setFormatter(file_formatter)
logger.addHandler(file_handler)


def read_json_file(path: str) -> list[dict]:
    """
    Читает JSON-файл и возвращает список словарей.
    Если файл не найден, пустой или содержит не список — возвращается пустой список.
    """
    try:
        logger.info(f"get_operations: начало обработки файла: {path}")
        with open(path, "r", encoding="utf-8") as f:
            data = json.load(f)
    except (FileNotFoundError, json.decoder.JSONDecodeError):
        logger.exception(f"get_operations: ошибка при чтении файла {path}")
        return []

    if not isinstance(data, list):
        logger.error(f"get_operations: данные не являются списком, путь {path}")
        return []

    logger.info(f"get_operations: завершение работы, результат: {data}")
    return data


def read_csv_file(path: str) -> list[dict]:
    """
    Читает CSV-файл и возвращает список словарей.
    Если файл не найден, пустой или содержит не список — возвращается пустой список.
    """
    try:
        df = pd.read_csv(path)
        result = df.to_dict("records")
        return result
    except (FileNotFoundError, ValueError):
        return []


def read_excel_file(path: str) -> list[dict]:
    """
    Читает XLSX-файл и возвращает список словарей.
    Если файл не найден, пустой или содержит не список — возвращается пустой список.
    """
    try:
        df = pd.read_excel(path)
        result = df.to_dict("records")
        return result
    except (FileNotFoundError, ValueError):
        return []


def choose_file_format(path: str) -> list[dict]:
    """
    Выбирает нужный формат файла JSON/CSV/XLSX
    """
    if path.endswith(".json"):
        return read_json_file(path)
    elif path.endswith(".csv"):
        return read_csv_file(path)
    elif path.endswith(".xlsx"):
        return read_excel_file(path)
    else:
        raise ValueError(f"Неподдерживаемый формат файла: {path}. Ожидаемый формат - .json/.csv/.xlsx")
