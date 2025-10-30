def filter_by_state(my_list: list[dict], state: str = "EXECUTED") -> list[dict]:
    """
    Принимаем список словарей, возвращает только те, у которых есть значение EXECUTED
    """
    filtered_list = []
    for item in my_list:
        if item.get("state") == state:
            filtered_list.append(item)
    return filtered_list


def sort_by_date(my_list: list[dict], ascending: bool = True) -> list[dict]:
    """
    Принимаем список словарей и сортирует их по дате
    """
    sorted_list = sorted(my_list, key=lambda item: item["date"], reverse=ascending)
    return sorted_list
