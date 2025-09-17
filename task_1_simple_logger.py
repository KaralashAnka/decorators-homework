#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Задание 1. Простой декоратор logger
"""

import os
from datetime import datetime
from functools import wraps


def logger(old_function):
    """
    Декоратор, который записывает в файл 'main.log':
    - дату и время вызова функции
    - имя функции
    - аргументы, с которыми вызвалась
    - возвращаемое значение
    """

    @wraps(old_function)
    def new_function(*args, **kwargs):
        # Вызываем оригинальную функцию и получаем результат
        result = old_function(*args, **kwargs)

        # Формируем строку с информацией о вызове
        timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        function_name = old_function.__name__

        # Форматируем аргументы для записи
        args_str = ', '.join(map(str, args))
        kwargs_str = ', '.join([f'{k}={v}' for k, v in kwargs.items()])

        # Объединяем все аргументы
        all_args = []
        if args_str:
            all_args.append(args_str)
        if kwargs_str:
            all_args.append(kwargs_str)
        args_combined = ', '.join(all_args)

        # Формируем строку для записи в лог
        log_entry = f"{timestamp} - {function_name}({args_combined}) -> {result}\n"

        # Записываем в файл main.log
        with open('main.log', 'a', encoding='utf-8') as log_file:
            log_file.write(log_entry)

        return result

    return new_function


def test_1():
    """Тестирование простого декоратора logger"""

    path = 'main.log'
    if os.path.exists(path):
        os.remove(path)

    @logger
    def hello_world():
        return 'Hello World'

    @logger
    def summator(a, b=0):
        return a + b

    @logger
    def div(a, b):
        return a / b

    assert 'Hello World' == hello_world(), "Функция возвращает 'Hello World'"
    result = summator(2, 2)
    assert isinstance(result, int), 'Должно вернуться целое число'
    assert result == 4, '2 + 2 = 4'
    result = div(6, 2)
    assert result == 3, '6 / 2 = 3'

    assert os.path.exists(path), 'файл main.log должен существовать'

    summator(4.3, b=2.2)
    summator(a=0, b=0)

    with open(path) as log_file:
        log_file_content = log_file.read()

    assert 'summator' in log_file_content, 'должно записаться имя функции'
    for item in (4.3, 2.2, 6.5):
        assert str(item) in log_file_content, f'{item} должен быть записан в файл'

    print("✅ Все тесты для задания 1 прошли успешно!")
    print(f"📄 Содержимое файла {path}:")
    print("-" * 50)
    print(log_file_content)


if __name__ == '__main__':
    test_1()