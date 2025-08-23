#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Тестовые примеры для программы поиска элементов больше заданного числа.
Тесты покрывают все ветви алгоритма.

Автор: Практика
Дата: 2024
"""

from main import find_elements_greater_than

def run_test_case(test_name, array, threshold, expected_count, expected_product):
    """
    Запускает тестовый пример и проверяет результат.
    
    Args:
        test_name (str): Название теста
        array (list): Тестовый массив
        threshold (float): Число для сравнения
        expected_count (int): Ожидаемое количество элементов
        expected_product (float): Ожидаемое произведение
    """
    print(f"\n{'='*60}")
    print(f"ТЕСТ: {test_name}")
    print(f"{'='*60}")
    
    print(f"Массив A: {array}")
    print(f"Число B: {threshold}")
    print(f"Ожидаемый результат: count={expected_count}, product={expected_product}")
    
    # Выполнение теста
    actual_count, actual_product = find_elements_greater_than(array, threshold)
    
    print(f"Фактический результат: count={actual_count}, product={actual_product}")
    
    # Проверка результатов
    count_correct = actual_count == expected_count
    product_correct = abs(actual_product - expected_product) < 1e-10  # Учет погрешности для float
    
    if count_correct and product_correct:
        print("✅ ТЕСТ ПРОЙДЕН")
    else:
        print("❌ ТЕСТ НЕ ПРОЙДЕН")
        if not count_correct:
            print(f"   Ошибка в count: ожидалось {expected_count}, получено {actual_count}")
        if not product_correct:
            print(f"   Ошибка в product: ожидалось {expected_product}, получено {actual_product}")

def main():
    """
    Запуск всех тестовых примеров.
    """
    print("ЗАПУСК ТЕСТОВЫХ ПРИМЕРОВ")
    print("="*60)
    
    # Тест 1: Все элементы больше B
    # Ветвь: все элементы проходят условие A[i] > B
    run_test_case(
        "Все элементы больше B",
        [5, 10, 15, 20],
        3,
        4,
        5 * 10 * 15 * 20
    )
    
    # Тест 2: Все элементы меньше или равны B
    # Ветвь: ни один элемент не проходит условие A[i] > B
    run_test_case(
        "Все элементы меньше или равны B",
        [1, 2, 3, 4],
        5,
        0,
        1
    )
    
    # Тест 3: Некоторые элементы больше B
    # Ветвь: смешанный случай - некоторые элементы проходят условие
    run_test_case(
        "Некоторые элементы больше B",
        [1, 5, 2, 8, 3, 10],
        4,
        3,
        5 * 8 * 10
    )
    
    # Тест 4: Пустой массив
    # Ветвь: массив пустой, цикл не выполняется
    run_test_case(
        "Пустой массив",
        [],
        5,
        0,
        1
    )
    
    # Тест 5: Один элемент, равный B
    # Ветвь: элемент не проходит условие A[i] > B
    run_test_case(
        "Один элемент, равный B",
        [5],
        5,
        0,
        1
    )
    
    # Тест 6: Один элемент, больше B
    # Ветвь: элемент проходит условие A[i] > B
    run_test_case(
        "Один элемент, больше B",
        [7],
        5,
        1,
        7
    )
    
    # Тест 7: Отрицательные числа
    # Ветвь: работа с отрицательными числами
    run_test_case(
        "Отрицательные числа",
        [-5, -2, 0, 3, 7],
        -3,
        4,
        (-2) * 0 * 3 * 7
    )
    
    # Тест 8: Дробные числа
    # Ветвь: работа с дробными числами
    run_test_case(
        "Дробные числа",
        [1.5, 2.7, 3.2, 4.1],
        2.5,
        3,
        2.7 * 3.2 * 4.1
    )
    
    # Тест 9: Нулевые элементы
    # Ветвь: работа с нулевыми элементами
    run_test_case(
        "Нулевые элементы",
        [0, 1, 0, 5, 0],
        0,
        2,
        1 * 5
    )
    
    # Тест 10: Большие числа
    # Ветвь: работа с большими числами
    run_test_case(
        "Большие числа",
        [1000, 2000, 3000, 4000],
        1500,
        3,
        2000 * 3000 * 4000
    )
    
    print(f"\n{'='*60}")
    print("ТЕСТИРОВАНИЕ ЗАВЕРШЕНО")
    print("="*60)

if __name__ == "__main__":
    main() 