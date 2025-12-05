import os

import requests
from dotenv import load_dotenv

load_dotenv()
API_KEY = os.getenv("API_KEY")


def get_amount_rub(transaction: dict) -> float:
    """
    Принимает словарь с транзакциями и возвращает сумму в рублях.
    Если валюта RUB - возвращает напрямую сумму.
    Если валюта USD/EUR - конвертирует актуальные данные через API get /convert.
    """
    amount = float(transaction.get("amount", 0))
    currency = transaction.get("currency", "RUB")

    if currency == "RUB":
        return amount

    if not API_KEY:
        return 0.0

    url = "https://api.apilayer.com/exchangerates_data/convert"
    params = {"from": currency, "to": "RUB", "amount": amount}
    headers = {"apikey": API_KEY}

    try:
        response = requests.get(url, headers=headers, params=params)
        data = response.json()

        if not data.get("success"):
            return 0.0

        return float(data.get("result", 0.0))

    except (requests.RequestException, ValueError, KeyError):
        return 0.0
