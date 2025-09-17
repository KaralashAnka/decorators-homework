#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Демонстрация всех заданий по декораторам
"""

import os
import subprocess
import sys


def run_task(task_file, task_name):
    """Запуск задания и показ результатов"""
    print(f"\n{'=' * 60}")
    print(f"🎯 ВЫПОЛНЯЕТСЯ: {task_name}")
    print(f"📁 Файл: {task_file}")
    print('=' * 60)

    try:
        # Запускаем Python скрипт
        result = subprocess.run([sys.executable, task_file],
                                capture_output=True,
                                text=True,
                                encoding='utf-8')

        if result.stdout:
            print("📤 ВЫВОД:")
            print(result.stdout)

        if result.stderr:
            print("❌ ОШИБКИ:")
            print(result.stderr)

        if result.returncode == 0:
            print("✅ Задание выполнено успешно!")
        else:
            print(f"❌ Задание завершилось с кодом {result.returncode}")

    except Exception as e:
        print(f"💥 Ошибка при запуске: {e}")


def show_file_structure():
    """Показать структуру файлов проекта"""
    print("\n📁 СТРУКТУРА ПРОЕКТА:")
    print("=" * 40)

    files_to_show = [
        "task_1_simple_logger.py",
        "task_2_parametrized_logger.py",
        "decorators.py",
        "main.py",
        "application/salary.py",
        "application/db/people.py",
        "test_decorators.py"
    ]

    for file in files_to_show:
        if os.path.exists(file):
            print(f"✅ {file}")
        else:
            print(f"❌ {file} - НЕ НАЙДЕН")


def show_generated_logs():
    """Показать все созданные лог-файлы"""
    print(f"\n📄 СОЗДАННЫЕ ЛОГ-ФАЙЛЫ:")
    print("=" * 40)

    log_extensions = ['.log']
    log_files = []

    # Ищем все .log файлы в текущей директории
    for file in os.listdir('.'):
        if any(file.endswith(ext) for ext in log_extensions):
            log_files.append(file)

    if log_files:
        for log_file in sorted(log_files):
            size = os.path.getsize(log_file)
            print(f"📋 {log_file} ({size} bytes)")
    else:
        print("Лог-файлы не найдены")


def main():
    """Главная демонстрационная функция"""
    print("🎭 ДЕМОНСТРАЦИЯ ДОМАШНЕГО ЗАДАНИЯ ПО ДЕКОРАТОРАМ")
    print("=" * 60)
    print("Выполняем все задания по порядку...")

    # Показываем структуру проекта
    show_file_structure()

    # Задание 1: Простой декоратор
    if os.path.exists("task_1_simple_logger.py"):
        run_task("task_1_simple_logger.py", "Задание 1 - Простой декоратор logger")
    else:
        print("❌ Файл task_1_simple_logger.py не найден!")

    # Задание 2: Параметризованный декоратор
    if os.path.exists("task_2_parametrized_logger.py"):
        run_task("task_2_parametrized_logger.py", "Задание 2 - Параметризованный декоратор logger")
    else:
        print("❌ Файл task_2_parametrized_logger.py не найден!")

    # Задание 3: Применение к программе бухгалтерия
    print(f"\n{'=' * 60}")
    print("🎯 ЗАДАНИЕ 3 - Применение логгера к программе 'Бухгалтерия'")
    print('=' * 60)

    if os.path.exists("main.py"):
        run_task("main.py", "Обновленная программа Бухгалтерия с декораторами")
    else:
        print("❌ Файл main.py не найден!")

    # Дополнительное тестирование
    if os.path.exists("test_decorators.py"):
        run_task("test_decorators.py", "Расширенное тестирование декораторов")
    else:
        print("❌ Файл test_decorators.py не найден!")

    # Показываем созданные логи
    show_generated_logs()

    print(f"\n{'🎉' * 20}")
    print("ВСЕ ЗАДАНИЯ ВЫПОЛНЕНЫ!")
    print("Проверьте созданные лог-файлы для анализа работы декораторов.")
    print(f"{'🎉' * 20}")


if __name__ == '__main__':
    main()