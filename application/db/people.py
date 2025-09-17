#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Модуль для работы с данными сотрудников с применением декораторов
"""

import time
from datetime import datetime
from decorators import logger, performance_monitor, validate_args


@logger('accounting.log')
@performance_monitor
def get_employees():
    """
    Функция для получения списка сотрудников
    """
    print("👥 Загружаем список сотрудников из базы данных...")
    print("   - Подключение к базе данных")
    print("   - Выборка активных сотрудников")
    print("   - Проверка актуальности данных")

    # Имитируем задержку загрузки данных
    time.sleep(0.05)

    # Имитируем возвращение списка сотрудников
    employees = [
        {"id": 1, "name": "Иванов И.И.", "position": "Менеджер", "salary": 120000.0},
        {"id": 2, "name": "Петров П.П.", "position": "Программист", "salary": 180000.0},
        {"id": 3, "name": "Сидоров С.С.", "position": "Аналитик", "salary": 150000.0}
    ]

    print(f"✅ Загружено {len(employees)} сотрудников")
    print(f"   Время загрузки: {datetime.now().strftime('%H:%M:%S')}")

    return employees


@logger('accounting.log')
@validate_args(int)
def get_employee_by_id(employee_id):
    """
    Получить сотрудника по ID

    Args:
        employee_id (int): ID сотрудника
    """
    employees = get_employees()

    for employee in employees:
        if employee['id'] == employee_id:
            print(f"🔍 Найден сотрудник: {employee['name']}")
            return employee

    print(f"❌ Сотрудник с ID {employee_id} не найден")
    return None


@logger('accounting.log')
@validate_args(str, str)
def add_employee(name, position):
    """
    Добавить нового сотрудника

    Args:
        name (str): Имя сотрудника
        position (str): Должность
    """
    if not name.strip():
        raise ValueError("Имя сотрудника не может быть пустым")

    if not position.strip():
        raise ValueError("Должность не может быть пустой")

    # Имитируем добавление в базу данных
    new_employee = {
        'id': 4,  # В реальности генерировался бы автоматически
        'name': name.strip(),
        'position': position.strip(),
        'salary': 100000.0,  # Базовая зарплата
        'hire_date': datetime.now().strftime('%Y-%m-%d')
    }

    print(f"➕ Добавлен новый сотрудник: {name} - {position}")
    return new_employee


@logger('accounting.log')
def update_employee_data():
    """
    Дополнительная функция для обновления данных сотрудников
    """
    update_info = {
        'updated_at': datetime.now().isoformat(),
        'records_updated': 3,
        'status': 'success'
    }

    print("🔄 Данные сотрудников обновлены")
    return update_info


@logger('accounting.log')
def get_employees_by_position(position):
    """
    Получить сотрудников по должности

    Args:
        position (str): Должность для поиска
    """
    if not isinstance(position, str):
        raise TypeError("Должность должна быть строкой")

    employees = get_employees()
    filtered_employees = [
        emp for emp in employees
        if emp['position'].lower() == position.lower()
    ]

    print(f"🎯 Найдено {len(filtered_employees)} сотрудников с должностью '{position}'")
    return filtered_employees


@logger('accounting.log')
def calculate_department_stats():
    """
    Рассчитать статистику по отделам
    """
    employees = get_employees()

    # Группируем по должностям
    positions = {}
    total_salary = 0

    for emp in employees:
        pos = emp['position']
        salary = emp.get('salary', 0)

        if pos not in positions:
            positions[pos] = {'count': 0, 'total_salary': 0}

        positions[pos]['count'] += 1
        positions[pos]['total_salary'] += salary
        total_salary += salary

    # Вычисляем средние зарплаты
    for pos_data in positions.values():
        pos_data['average_salary'] = pos_data['total_salary'] / pos_data['count']

    stats = {
        'total_employees': len(employees),
        'total_salary_budget': total_salary,
        'average_salary': total_salary / len(employees) if employees else 0,
        'positions': positions,
        'generated_at': datetime.now().isoformat()
    }

    print("📈 Статистика по отделам рассчитана")
    return stats