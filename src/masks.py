def get_mask_card_number(card_number: str | int) -> str:
    """
    Принимаем номер карты, возвращает замаскированный номер
    """
    card = str(card_number)
    if len(card) < 16:
        return "Неверные данные"
    start_of_number = card[:6]
    end_of_number = card[-4:]
    middle_of_number = "*" * (len(card) - 10)
    masked = start_of_number + middle_of_number + end_of_number
    parts = []
    for i in range(0, len(masked), 4):
        parts.append(masked[i : i + 4])
    return " ".join(parts)


def get_mask_account(account_number: str | int) -> str:
    """
    Принимаем номер счета и возвращает замаскированный номер
    """
    number = str(account_number)
    if len(number) < 20:
        return "Неверные данные"
    end_of_number = number[-4:]
    rest_of_number = "**"
    masked = rest_of_number + end_of_number
    return masked
