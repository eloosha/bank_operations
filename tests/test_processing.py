import pytest

from src.processing import filter_by_state, process_bank_operations, process_bank_search, sort_by_date


# Фикстуры и тесты для filter_by_state
@pytest.fixture
def sample_data():
    return [
        {"state": "EXECUTED", "date": "2024-03-01"},
        {"state": "CANCELED", "date": "2023-07-11"},
        {"state": "EXECUTED", "date": "2025-01-01"},
        {"state": "CANCELED", "date": "2022-06-05"},
    ]


def test_filter_by_state(sample_data):
    result = filter_by_state(sample_data)
    assert len(result) == 2


@pytest.mark.parametrize("state, expected_count", [("EXECUTED", 2), ("CANCELED", 2)])
def test_filter_by_state_parameters(sample_data, state, expected_count):
    result = filter_by_state(sample_data)
    assert len(result) == expected_count


# Тесты для sort_by_date
def test_sort_by_date_desc(sample_data):
    result = sort_by_date(sample_data, descending=True)
    assert result[0]["date"] == "2025-01-01"
    assert result[-1]["date"] == "2022-06-05"


def test_sort_by_date_asc(sample_data):
    result = sort_by_date(sample_data, descending=False)
    assert result[0]["date"] == "2022-06-05"
    assert result[-1]["date"] == "2025-01-01"


# Тест для process_bank_search
def test_process_bank_search_basic():
    data = [
        {"description": "Перевод организации", "id": 1},
        {"description": "Перевод с карты на карту", "id": 2},
        {"description": "Открытие вклада", "id": 3},
    ]

    result = process_bank_search(data, "перевод")
    assert len(result) == 2
    assert all("перевод" in item["description"].lower() for item in result)


def test_process_bank_search_no_match():
    data = [
        {"description": "Перевод организации", "id": 1},
        {"description": "Открытие вклада", "id": 2},
    ]

    result = process_bank_search(data, "снятие")
    assert result == []


# Тест для process_bank_operations
def test_process_bank_operations_basic():
    data = [
        {"description": "Перевод организации"},
        {"description": "Перевод организации"},
        {"description": "Открытие вклада"},
    ]
    categories = ["Перевод организации", "Открытие вклада", "Снятие наличных"]

    result = process_bank_operations(data, categories)

    assert result == {"Перевод организации": 2, "Открытие вклада": 1, "Снятие наличных": 0}


def test_process_bank_operations_empty_data():
    data = []
    categories = ["Перевод организации", "Открытие вклада"]

    result = process_bank_operations(data, categories)

    assert result == {"Перевод организации": 0, "Открытие вклада": 0}
