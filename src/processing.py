def filter_by_state(my_list: list[dict], state: str = "EXECUTED") -> list[dict]:
    """
    Принимает список словарей, возвращает только те, у которых есть значение EXECUTED
    """
    filtered_list = []
    for item in my_list:
        if item.get("state") == state:
            filtered_list.append(item)
    return filtered_list


def sort_by_date(records: list[dict], descending: bool = True) -> list[dict]:
    """
    Принимает список словарей и сортирует их по дате
    """
    sorted_list = sorted(records, key=lambda rec: rec["date"], reverse=descending)
    return sorted_list
