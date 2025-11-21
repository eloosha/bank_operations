from typing import Iterator


def filter_by_currency(transactions: list[dict], currency_code: str) -> Iterator[dict]:
    """
    Принимает список словарей транзакций,
    возвращает итератор который поочередно выдает транзакции с валютой 'USD'
    """
    for transaction in transactions:
        transaction_code = transaction["operationAmount"]["currency"]["code"]
        if transaction_code == currency_code:
            yield transaction


def transaction_descriptions(transactions: list[dict]) -> Iterator[str]:
    """
    Принимает список словарей транзакций,
    возвращает итератор который поочередно выдает описание транзакции
    """
    for transaction in transactions:
        transaction_description = transaction["description"]
        yield transaction_description


def card_number_generator(start: int, end: int) -> Iterator[str]:
    """
    Генерирует номера банковских карт в формате XXXX XXXX XXXX XXXX
    """
    for number in range(start, end + 1):
        card_number = str(number)
        card_number = "0" * (16 - len(card_number)) + card_number

        parts = []
        for i in range(0, 16, 4):
            parts.append(card_number[i : i + 4])

        formatted = " ".join(parts)
        yield formatted
