import re
from collections import Counter


def filter_by_state(my_list: list[dict], state: str = "EXECUTED") -> list[dict]:
    """
    Принимает список словарей, возвращает список по ключевому слову EXECUTED/CANCELED/PENDING.
    Если ничего не указано, то дефолт - EXECUTED.
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


def process_bank_search(data: list[dict], search: str) -> list[dict]:
    '''
    Функция проходит по данным с операциями и возвращает список словарей
    по ключевому слову в описании операций ('description')
    '''
    search_result = []
    pattern = re.compile(search, re.IGNORECASE)

    for item in data:
        if pattern.search(item.get('description', '')):
            search_result.append(item)
    return search_result


def process_bank_operations(data: list[dict], categories: list) -> dict:
    '''
    Принимает список операций и список категорий, выводит словарь категорий и
    их количество в списке операций.
    '''
    filtered_descriptions = [item["description"] for item in data if item['description'] in categories]

    counter = Counter(filtered_descriptions)

    for category in categories:
        if category not in counter:
            counter[category] = 0

    return dict(counter)
