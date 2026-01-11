import logging
from typing import Union

logger = logging.getLogger("masks")
logger.setLevel(logging.DEBUG)
file_handler = logging.FileHandler("logs/masks.log", mode="w", encoding="utf-8")
file_formatter = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s")
file_handler.setFormatter(file_formatter)
logger.addHandler(file_handler)


def get_mask_card_number(card_number: Union[str, int]) -> str:
    """
    Принимаем номер карты, возвращает замаскированный номер
    """
    try:
        logger.info(f"get_mask_card_number: начало обработки номера карты {card_number}")
        card = str(card_number)
        if len(card) < 16:
            logger.error(f"get_mask_card_number: неверные данные: {card_number}")
            return "Неверные данные"
        start_of_number = card[:6]
        end_of_number = card[-4:]
        middle_of_number = "*" * (len(card) - 10)
        masked = start_of_number + middle_of_number + end_of_number
        parts = []
        for i in range(0, len(masked), 4):
            parts.append(masked[i : i + 4])
        logger.info(f'get_mask_card_number: результат маскировки: {" ".join(parts)}')
        return " ".join(parts)
    except Exception as ex:
        logger.exception(f"Возникла ошибка: {ex}")
        return "Неверные данные"


def get_mask_account(account_number: Union[str, int]) -> str:
    """
    Принимаем номер счета и возвращает замаскированный номер
    """
    try:
        logger.info(f"get_mask_account: начало обработки номера счета {account_number}")
        number = str(account_number)
        if len(number) < 20:
            logger.error(f"get_mask_account: неверные данные: {account_number}")
            return "Неверные данные"
        end_of_number = number[-4:]
        rest_of_number = "**"
        masked = rest_of_number + end_of_number
        logger.info(f"get_mask_account: результат маскировки: {masked}")
        return masked
    except Exception as ex:
        logger.exception(f"Возникла ошибка: {ex}")
        return "Неверные данные"
