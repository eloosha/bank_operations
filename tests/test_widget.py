import pytest

from src.widget import mask_account_card


# Тесты для mask_account_card
@pytest.mark.parametrize(
    "input_string, expected",
    [
        ("Visa Classic 1234567812345678", "Visa Classic 1234 56** **** 5678"),
        ("Счет 40817810099910004312", "Счет **4312"),
        ("Maestro 123", "Неверные данные"),
    ],
)
def test_mask_account_card(input_string, expected):
    assert mask_account_card(input_string) == expected
