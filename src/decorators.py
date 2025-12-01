from typing import Any, Callable, Optional


def log(filename: Optional[str] = None) -> Callable:
    """
    Декоратор для логирования вызовов функции.

    Если указан filename, логи записываются в файл.
    Если filename не указан — выводятся только в консоль.

    Логируются:
    - старт выполнения функции
    - успешное завершение и результат
    - исключения с аргументами, при их возникновении
    """

    def decorator(func: Callable) -> Callable:
        def wrapper(*args: Any, **kwargs: Any) -> Any:
            """
            Обёртка, выполняющая логирование перед, после и при ошибке
            исходной функции.
            """
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
