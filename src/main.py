from src.generators import filter_by_currency
from src.processing import filter_by_state, process_bank_operations, process_bank_search, sort_by_date
from src.utils import choose_file_format, read_json_file


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

    # Получаем данные через choose_file_format
    while True:
        path = input("Введите путь к файлу с транзакциями: ").strip()
        try:
            data = choose_file_format(path)
            break
        except ValueError as e:
            print("Неверный путь к файлу. Попробуйте ввести путь ещё раз. ")

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

    data = list(data)
    print(f"\nКоличество операций по категориям: {len(data)}")

    for item in data:
        date = item["date"][:10]
        description = item["description"]
        amount = item["operationAmount"]["amount"]
        currency = item["operationAmount"]["currency"]["name"]

        print(f"{date} {description}")
        print(f"Сумма: {amount} {currency}\n")


if __name__ == "__main__":
    main()
