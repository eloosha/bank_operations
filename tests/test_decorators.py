import pytest

from src.decorators import log


def test_log_successful(capsys):
    @log()
    def divide(a, b):
        return a / b

    with pytest.raises(ZeroDivisionError):
        divide(1, 0)

    result = divide(8, 4)
    assert result == 2
    captured = capsys.readouterr()
    assert "Ошибка в функции divide: division by zero" in captured.out
    assert "Функция divide завершилась успешно. Результат: 2" in captured.out
    assert "Начало выполнения функции: divide" in captured.out
    assert "Конец выполнения функции: divide" in captured.out


def test_log_error(capsys):
    @log()
    def square(x):
        return x * x

    result = square(3)
    assert result == 9
    captured = capsys.readouterr()
    assert "Начало выполнения функции: square" in captured.out
    assert "Конец выполнения функции: square" in captured.out


def test_log_to_file():
    filename = "test_log.txt"

    @log(filename=filename)
    def add(a, b):
        return a + b

    result = add(5, 3)
    assert result == 8

    with open(filename, "r", encoding="utf-8") as f:
        content = f.read()

    assert "Функция add завершилась успешно. Результат: 8" in content
    assert "Начало выполнения функции: add" in content
    assert "Конец выполнения функции: add" in content

    import os

    os.remove(filename)
