#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Задание 2. Параметризованный декоратор logger
"""

import os
from datetime import datetime
from functools import wraps


def logger(path):
    """
    Параметризованный декоратор, который записывает в указанный файл:
    - дату и время вызова функции
    - имя функции
    - аргументы, с которыми вызвалась
    - возвращаемое значение

    Args:
        path (str): Путь к файлу для записи логов
    """

    def __logger(old_function):
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

            # Записываем в указанный файл
            with open(path, 'a', encoding='utf-8') as log_file:
                log_file.write(log_entry)

            return result

        return new_function

    return __logger


def test_2():
    """Тестирование параметризованного декоратора logger"""

    paths = ('log_1.log', 'log_2.log', 'log_3.log')

    for path in paths:
        if os.path.exists(path):
            os.remove(path)

        @logger(path)
        def hello_world():
            return 'Hello World'

        @logger(path)
        def summator(a, b=0):
            return a + b

        @logger(path)
        def div(a, b):
            return a / b

        assert 'Hello World' == hello_world(), "Функция возвращает 'Hello World'"
        result = summator(2, 2)
        assert isinstance(result, int), 'Должно вернуться целое число'
        assert result == 4, '2 + 2 = 4'
        result = div(6, 2)
        assert result == 3, '6 / 2 = 3'
        summator(4.3, b=2.2)

    for path in paths:
        assert os.path.exists(path), f'файл {path} должен существовать'

        with open(path) as log_file:
            log_file_content = log_file.read()

        assert 'summator' in log_file_content, 'должно записаться имя функции'

        for item in (4.3, 2.2, 6.5):
            assert str(item) in log_file_content, f'{item} должен быть записан в файл'

    print("✅ Все тесты для задания 2 прошли успешно!")

    # Показываем содержимое всех лог-файлов
    for path in paths:
        print(f"\n📄 Содержимое файла {path}:")
        print("-" * 50)
        with open(path) as log_file:
            print(log_file.read())


if __name__ == '__main__':
    test_2()