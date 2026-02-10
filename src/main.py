from pathlib import Path

from src.generators import filter_by_currency
from src.processing import filter_by_state, process_bank_search, sort_by_date
from src.utils import choose_file_format

from src.widget import mask_account_card

BASE_DIR = Path(__file__).resolve().parent.parent
DATA_DIR = BASE_DIR / "data"

data_path_json = str(DATA_DIR / "operations.json")
data_path_csv = str(DATA_DIR / "transactions.csv")
data_path_xlsx = str(DATA_DIR / "transactions_excel.xlsx")


def main():
    # Начало программы
    print(
        """
    Привет! Добро пожаловать в программу работы с банковскими транзакциями. 
    Выберите необходимый пункт меню: 
    1. Получить информацию о транзакциях из JSON-файла
    2. Получить информацию о транзакциях из CSV-файла
    3. Получить информацию о транзакциях из XLSX-файла
    """
    )
    # Выбор типа файла
    while True:
        user_choice = input().strip()
        if user_choice not in ("1", "2", "3"):
            print("Выберите пункт 1, 2 или 3. ")
        else:
            break

    if user_choice == "1":
        print("Для обработки выбран JSON-файл")
        data = choose_file_format(data_path_json)

    if user_choice == "2":
        print("Для обработки выбран CSV-файл")
        data = choose_file_format(data_path_csv)

    if user_choice == "3":
        print("Для обработки выбран XLSX-файл")
        data = choose_file_format(data_path_xlsx)

    # Приводим CSV и XLSX в единый формат
    if user_choice in ("2", "3"):
        normalized_data = []
        for row in data:
            item = {
                "id": row["id"],
                "state": row["state"],
                "date": row["date"],
                "from": row["from"],
                "to": row['to'],
                "description": row["description"],
                "operationAmount": {
                    "amount": row["amount"],
                    "currency": {
                        "name": row["currency_name"],
                        "code": row["currency_code"],
                    },
                },
            }
            normalized_data.append(item)
        data = normalized_data

    # Фильтрация по статусу
    valid_statuses = ("EXECUTED", "CANCELED", "PENDING")

    while True:
        status = input("Введите статус для фильтрации (EXECUTED, CANCELED, PENDING): ").strip().upper()

        if status in valid_statuses:
            data = filter_by_state(data, status)
            print(f'Операции отфильтрованы по статусу "{status}"')
            break
        print(f'Статус "{status}" недоступен. ')

    # Сортировка по дате
    while True:
        sort_answer = input("Отсортировать операции по дате? Да/Нет: ").strip().lower()
        if sort_answer in ("да", "нет"):
            break
        print('Пожалуйста, введите "Да" или "Нет". ')

    if sort_answer == "да":
        while True:
            order = input("По возрастанию или по убыванию?: ").strip().lower()
            if order in ("по возрастанию", "по убыванию"):
                descending = order == "по убыванию"
                data = sort_by_date(data, descending=descending)
                break
            print('Введите "по возрастанию" или "по убыванию". ')

    # Фильтрация по валюте
    while True:
        currency_type = input("Выводить только рублевые транзакции? Да/Нет: ").strip().lower()
        if currency_type in ("да", "нет"):
            if currency_type == "да":
                data = filter_by_currency(data, "RUB")
            break
        print('Пожалуйста, введите "Да" или "Нет". ')

    # Поиск по описанию
    while True:
        users_description = input("Отфильтровать по слову в описании? Да/Нет: ").strip().lower()
        if users_description in ("да", "нет"):
            if users_description == "да":
                word = input("Введите слово для поиска: ").strip()
                data = process_bank_search(data, word)
            break
        print('Пожалуйста, введите "Да" или "Нет". ')

    # Вывод
    if not data:
        print("Не найдено ни одной транзакции, подходящей под ваши условия фильтрации")
        return

    # Приводим дату к типу данных список, создаем переменные для принта
    data = list(data)
    print(f"\nВсего банковских операций в выборке: {len(data)}")

    for item in data:
        date = item["date"][:10]
        description = item["description"]
        amount = item["operationAmount"]["amount"]
        currency = item["operationAmount"]["currency"]["name"]
        from_raw = item.get("from", "")
        to_raw = item.get("to", "")
        from_ = mask_account_card(str(from_raw)) if from_raw else ''
        to_ = mask_account_card(str(to_raw)) if to_raw else ''

        # Принтуем данные
        print(f"{date} {description}")
        if from_ and to_:
            print(f"{from_} -> {to_}")
        elif from_:
            print(from_)
        elif to_:
            print(to_)
        else:
            return
        print(f"Сумма: {amount} {currency}\n")


if __name__ == "__main__":
    main()
