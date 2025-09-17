#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Модуль с декораторами для программы "Бухгалтерия"
"""

from datetime import datetime
from functools import wraps
import os


def logger(path_or_function=None):
    """
    Универсальный декоратор логирования.
    Может использоваться как простой декоратор (@logger)
    или как параметризованный (@logger('path/to/file.log'))

    Args:
        path_or_function: Путь к файлу логов или декорируемая функция
    """

    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            # Определяем путь к файлу логов
            if isinstance(path_or_function, str):
                log_path = path_or_function
            else:
                log_path = 'accounting.log'

            # Получаем время начала выполнения
            start_time = datetime.now()

            try:
                # Вызываем оригинальную функцию
                result = func(*args, **kwargs)

                # Рассчитываем время выполнения
                end_time = datetime.now()
                execution_time = (end_time - start_time).total_seconds()

                # Формируем строку с аргументами
                args_str = ', '.join(map(str, args))
                kwargs_str = ', '.join([f'{k}={v}' for k, v in kwargs.items()])

                all_args = []
                if args_str:
                    all_args.append(args_str)
                if kwargs_str:
                    all_args.append(kwargs_str)
                args_combined = ', '.join(all_args)

                # Формируем запись в лог
                log_entry = (
                    f"{start_time.strftime('%Y-%m-%d %H:%M:%S')} | "
                    f"SUCCESS | {func.__name__}({args_combined}) -> {result} | "
                    f"Время: {execution_time:.4f}с\n"
                )

                # Записываем в файл
                with open(log_path, 'a', encoding='utf-8') as log_file:
                    log_file.write(log_entry)

                return result

            except Exception as e:
                # Логируем ошибки
                end_time = datetime.now()
                execution_time = (end_time - start_time).total_seconds()

                log_entry = (
                    f"{start_time.strftime('%Y-%m-%d %H:%M:%S')} | "
                    f"ERROR | {func.__name__}({args}, {kwargs}) -> {type(e).__name__}: {e} | "
                    f"Время: {execution_time:.4f}с\n"
                )

                with open(log_path, 'a', encoding='utf-8') as log_file:
                    log_file.write(log_entry)

                # Перебрасываем исключение
                raise

        return wrapper

    # Проверяем, использован ли декоратор без параметров
    if callable(path_or_function):
        return decorator(path_or_function)
    else:
        return decorator


def performance_monitor(func):
    """
    Декоратор для мониторинга производительности функций
    """

    @wraps(func)
    def wrapper(*args, **kwargs):
        start_time = datetime.now()
        result = func(*args, **kwargs)
        end_time = datetime.now()

        execution_time = (end_time - start_time).total_seconds()

        if execution_time > 1.0:  # Если функция выполнялась больше секунды
            print(f"⚠️  МЕДЛЕННОЕ ВЫПОЛНЕНИЕ: {func.__name__} заняла {execution_time:.2f} секунд")

        return result

    return wrapper


def validate_args(*types):
    """
    Декоратор для валидации типов аргументов
    """

    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            # Проверяем типы позиционных аргументов
            for i, (arg, expected_type) in enumerate(zip(args, types)):
                if not isinstance(arg, expected_type):
                    raise TypeError(
                        f"Аргумент {i + 1} функции {func.__name__} должен быть типа {expected_type.__name__}, "
                        f"получен {type(arg).__name__}"
                    )

            return func(*args, **kwargs)

        return wrapper

    return decorator