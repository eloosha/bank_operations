def log(filename=None):
    def decorator(func):
        def wrapper(*args, **kwargs):
            print(f"Начало выполнения функции: {func.__name__}")

            if filename is None:
                print("Файл не указан, поэтому лог не ведется")
            else:
                with open(filename, "a+", encoding="utf-8") as f:
                    f.write(f"Начало выполнения функции: {func.__name__}.\n")

            try:
                result = func(*args, **kwargs)
                print(f"Функция {func.__name__} завершилась успешно. Результат: {result}")
                if filename is not None:
                    with open(filename, "a+", encoding="utf-8") as f:
                        f.write(f"Функция {func.__name__} завершилась успешно. Результат: {result}\n")
                return result
            except Exception as error:
                print(f"Ошибка в функции {func.__name__}: {error}")
                if filename is not None:
                    with open(filename, "a+", encoding="utf-8") as f:
                        f.write(f"Ошибка в функции {func.__name__}: {error}\n")
                raise
            finally:
                print(f"Конец выполнения функции: {func.__name__}")
                if filename is not None:
                    with open(filename, "a+", encoding="utf-8") as f:
                        f.write(f"Конец выполнения функции: {func.__name__}\n")

        return wrapper

    return decorator
