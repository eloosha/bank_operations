import json
import logging
from pathlib import Path

logger = logging.getLogger("utils")
logger.setLevel(logging.DEBUG)
file_handler = logging.FileHandler("logs/utils.log", mode="w", encoding="utf-8")
file_formatter = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s")
file_handler.setFormatter(file_formatter)
logger.addHandler(file_handler)


def get_operations(path: str) -> list:
    """
    Читает JSON-файл с транзакциями и возвращает список словарей.
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
