def mask_account_card(card_info: str) -> str:
    """
    Принимаем тип и номер карты или счета, возвращаем замаскированный номер
    """
    string_number = ''
    string_name = ''
    for i in card_info:
        if i.isnumeric():
            string_number += i
        else:
            string_name += i

    if len(string_number) == 16:
        start_of_number = string_number[:6]
        end_of_number = string_number[-4:]
        middle_of_number = "*" * (len(string_number) - 10)
        masked = start_of_number + middle_of_number + end_of_number
        parts = []
        for i in range(0, len(masked), 4):
            parts.append(masked[i:i + 4])
        parts_combined = " ".join(parts)
        return string_name + parts_combined
    elif len(string_number) == 20:
        end_of_number = string_number[-4:]
        rest_of_number = "**"
        masked = rest_of_number + end_of_number
        return string_name + masked
    else:
        return 'Неверный номер'


def get_date(date: str) -> str:
    """
    Принимаем дату в определенном формате и преобразуем её в нужный для нас формат
    """
    return date[8:10] + '.' + date[5:7] + '.' + date[0:4]
