import pytest

from src.masks import get_mask_account, get_mask_card_number


# Фикстуры и тесты для get_mask_card_number
@pytest.fixture
def card_number():
    return "1234567812345678"


def test_get_mask_card_number_correct(card_number):
    assert get_mask_card_number(card_number) == "1234 56** **** 5678"


@pytest.mark.parametrize("invalid_card_number", ["123", "", 123])
def test_get_mask_card_number_invalid(invalid_card_number):
    assert get_mask_card_number(invalid_card_number) == "Неверные данные"


# Фикстуры и тесты для get_mask_account
@pytest.fixture
def account_number():
    return "40817810099910004312"


def test_get_mask_account_correct(account_number):
    assert get_mask_account(account_number) == "**4312"


@pytest.mark.parametrize("invalid_account_number", ["123", "", 123])
def test_get_mask_account_invalid(invalid_account_number):
    assert get_mask_account(invalid_account_number) == "Неверные данные"
