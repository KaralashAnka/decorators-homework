#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Модуль для расчета зарплаты сотрудников с применением декораторов
"""

import time
from datetime import datetime
from decorators import logger, performance_monitor, validate_args


@logger('accounting.log')
@performance_monitor
def calculate_salary():
    """
    Функция для расчета зарплаты сотрудников
    """
    print("🧮 Выполняется расчет зарплаты...")
    print("   - Обработка базовых окладов")
    print("   - Расчет премий и надбавок")
    print("   - Вычисление налогов и удержаний")
    print(f"   - Дата расчета: {datetime.now().strftime('%d.%m.%Y')}")

    # Имитируем сложные вычисления
    time.sleep(0.1)

    # Имитируем результат расчета
    salary_data = {
        'total_employees': 3,
        'total_salary': 450000.0,
        'average_salary': 150000.0
    }

    print("✅ Расчет зарплаты завершен!")
    return salary_data


@logger('accounting.log')
@validate_args(str, float, float)
def calculate_individual_salary(employee_name, base_salary, bonus_percent=0.0):
    """
    Расчет зарплаты для конкретного сотрудника

    Args:
        employee_name (str): Имя сотрудника
        base_salary (float): Базовая зарплата
        bonus_percent (float): Процент премии
    """
    bonus = base_salary * (bonus_percent / 100)
    total_salary = base_salary + bonus

    result = {
        'employee': employee_name,
        'base': base_salary,
        'bonus': bonus,
        'total': total_salary
    }

    print(f"💰 {employee_name}: {total_salary:.2f} руб. (базовая: {base_salary}, премия: {bonus:.2f})")
    return result


@logger('accounting.log')
def get_salary_report():
    """
    Дополнительная функция для генерации отчета по зарплате
    """
    report_data = {
        'report_date': datetime.now().strftime('%Y-%m-%d'),
        'status': 'generated',
        'format': 'detailed'
    }

    print("📊 Отчет по зарплате сгенерирован")
    return report_data


@logger('accounting.log')
def calculate_taxes(gross_salary):
    """
    Расчет налогов с зарплаты

    Args:
        gross_salary (float): Валовая зарплата
    """
    if not isinstance(gross_salary, (int, float)) or gross_salary < 0:
        raise ValueError("Зарплата должна быть положительным числом")

    income_tax = gross_salary * 0.13  # 13% подоходный налог
    social_tax = gross_salary * 0.22  # 22% социальные взносы

    net_salary = gross_salary - income_tax
    total_taxes = income_tax + social_tax

    return {
        'gross_salary': gross_salary,
        'income_tax': income_tax,
        'social_tax': social_tax,
        'net_salary': net_salary,
        'total_taxes': total_taxes
    }