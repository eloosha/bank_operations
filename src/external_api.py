import os

import requests
from dotenv import load_dotenv

load_dotenv()
API_KEY = os.getenv("API_KEY")


def get_amount_rub(transaction: dict) -> float:
    """
    Принимает словарь с транзакциями и возвращает сумму в рублях.
    Если валюта RUB - возвращает напрямую сумму.
    Если валюта USD/EUR - конвертирует актуальные данные через API.
    """
    amount = float(transaction.get("amount", 0))
    currency = transaction.get("currency", "RUB")

    if currency == "RUB":
        return amount

    if not API_KEY:
        return 0.0

    url = "https://api.apilayer.com/exchangerates_data/latest"
    headers = {"apikey": API_KEY}
    params = {"base": currency, "symbols": "RUB"}

    try:
        response = requests.get(url, headers=headers, params=params)
        data = response.json()
        rate = data.get("rates", {}).get("RUB")
        if rate is None:
            return 0.0
        return amount * float(rate)
    except (requests.RequestException, ValueError, KeyError):
        return 0.0
