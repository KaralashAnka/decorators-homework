#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Основной модуль программы "Бухгалтерия" с применением декораторов
"""

import os
from datetime import datetime
from decorators import logger, performance_monitor
from application.salary import calculate_salary
from application.db.people import get_employees


@logger('main_operations.log')
@performance_monitor
def main():
    """Основная функция программы"""
    print("=== Программа 'Бухгалтерия' с логированием ===")
    print(f"Дата запуска: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    print()

    # Получаем список сотрудников
    print("Получаем список сотрудников...")
    employees = get_employees()
    print()

    # Рассчитываем зарплату
    print("Рассчитываем зарплату...")
    salary_results = calculate_salary()
    print()

    print("Программа завершена успешно!")
    print(f"📄 Логи сохранены в файлы: main_operations.log, accounting.log")

    return "SUCCESS"


@logger
def show_logs():
    """Показать содержимое лог-файлов"""
    log_files = ['main_operations.log', 'accounting.log']

    for log_file in log_files:
        if os.path.exists(log_file):
            print(f"\n📄 Содержимое {log_file}:")
            print("-" * 60)
            with open(log_file, 'r', encoding='utf-8') as f:
                content = f.read()
                if content:
                    print(content)
                else:
                    print("Файл пустой")
        else:
            print(f"❌ Файл {log_file} не найден")


if __name__ == '__main__':
    main()
    print("\n" + "=" * 60)
    show_logs()