#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Тестирование всех декораторов и обновленной программы "Бухгалтерия"
"""

import os
from datetime import datetime
from decorators import logger
from application.salary import calculate_individual_salary, calculate_taxes
from application.db.people import get_employee_by_id, add_employee


def clean_log_files():
    """Очистка лог-файлов перед тестированием"""
    log_files = ['accounting.log', 'main_operations.log', 'test.log']
    for file in log_files:
        if os.path.exists(file):
            os.remove(file)
    print("🧹 Лог-файлы очищены")


@logger('test.log')
def test_accounting_functions():
    """Тестирование функций бухгалтерии с логированием"""
    print("🧪 Начинаем тестирование функций...")

    # Тест 1: Получение сотрудника по ID
    print("\n1. Тестируем получение сотрудника по ID:")
    employee = get_employee_by_id(1)
    print(f"   Результат: {employee}")

    # Тест 2: Добавление нового сотрудника
    print("\n2. Тестируем добавление сотрудника:")
    new_emp = add_employee("Кузнецов К.К.", "Дизайнер")
    print(f"   Результат: {new_emp}")

    # Тест 3: Расчет индивидуальной зарплаты
    print("\n3. Тестируем расчет зарплаты:")
    salary_result = calculate_individual_salary("Иванов И.И.", 120000.0, 15.0)
    print(f"   Результат: {salary_result}")

    # Тест 4: Расчет налогов
    print("\n4. Тестируем расчет налогов:")
    tax_result = calculate_taxes(150000.0)
    print(f"   Результат: {tax_result}")

    return "Все тесты завершены"


@logger('test.log')
def test_error_handling():
    """Тестирование обработки ошибок в декораторе"""
    print("⚠️ Тестируем обработку ошибок:")

    try:
        # Намеренно вызываем ошибку валидации типов
        calculate_individual_salary(123, "invalid", 10.0)  # Неправильные типы
    except TypeError as e:
        print(f"   Поймана ошибка типа: {e}")

    try:
        # Намеренно вызываем ошибку валидации значений
        calculate_taxes(-1000)  # Отрицательная зарплата
    except ValueError as e:
        print(f"   Поймана ошибка значения: {e}")

    return "Тестирование ошибок завершено"


def show_test_logs():
    """Показать содержимое тестовых логов"""
    log_files = ['test.log', 'accounting.log']

    for log_file in log_files:
        if os.path.exists(log_file):
            print(f"\n📄 Содержимое {log_file}:")
            print("=" * 60)
            with open(log_file, 'r', encoding='utf-8') as f:
                content = f.read()
                if content:
                    print(content)
                else:
                    print("Файл пустой")
        else:
            print(f"❌ Файл {log_file} не найден")


def main():
    """Основная функция для запуска всех тестов"""
    print("🚀 Запуск полного тестирования декораторов")
    print("=" * 60)

    # Очищаем старые логи
    clean_log_files()

    # Запускаем тесты
    test_result1 = test_accounting_functions()
    print(f"\n✅ {test_result1}")

    test_result2 = test_error_handling()
    print(f"✅ {test_result2}")

    # Показываем логи
    print("\n" + "=" * 60)
    print("РЕЗУЛЬТАТЫ ЛОГИРОВАНИЯ:")
    show_test_logs()

    print("\n" + "=" * 60)
    print("🎉 Тестирование завершено успешно!")


if __name__ == '__main__':
    main()