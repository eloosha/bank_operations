from src.masks import get_mask_card_number, get_mask_account


def mask_account_card(card_info: str) -> str:
    """
    Принимает строку с номером карты или счета,
    возвращает замаскированный номер с использованием функций из masks.py.
    """
    string_number = ""
    string_name = ""

    for i in card_info:
        if i.isdigit():
            string_number += i
        else:
            string_name += i

    if len(string_number) == 16:
        masked = get_mask_card_number(string_number)
    elif len(string_number) == 20:
        masked = get_mask_account(string_number)
    else:
        return "Неверные данные"
    return string_name.strip() + " " + masked

