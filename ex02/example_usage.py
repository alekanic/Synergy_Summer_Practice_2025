#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Пример использования программы для поиска элементов больше заданного числа.

Автор: Практика
Дата: 2024
"""

from main import find_elements_greater_than

def example_1():
    """
    Пример 1: Базовый случай
    """
    print("ПРИМЕР 1: Базовый случай")
    print("-" * 40)
    
    array = [1, 5, 3, 8, 2, 10]
    threshold = 4
    
    print(f"Массив: {array}")
    print(f"Число B: {threshold}")
    
    count, product = find_elements_greater_than(array, threshold)
    
    print(f"Результат:")
    print(f"  Количество элементов > {threshold}: {count}")
    print(f"  Произведение: {product}")
    print()

def example_2():
    """
    Пример 2: Все элементы больше B
    """
    print("ПРИМЕР 2: Все элементы больше B")
    print("-" * 40)
    
    array = [10, 20, 30, 40, 50]
    threshold = 5
    
    print(f"Массив: {array}")
    print(f"Число B: {threshold}")
    
    count, product = find_elements_greater_than(array, threshold)
    
    print(f"Результат:")
    print(f"  Количество элементов > {threshold}: {count}")
    print(f"  Произведение: {product}")
    print()

def example_3():
    """
    Пример 3: Ни один элемент не больше B
    """
    print("ПРИМЕР 3: Ни один элемент не больше B")
    print("-" * 40)
    
    array = [1, 2, 3, 4, 5]
    threshold = 10
    
    print(f"Массив: {array}")
    print(f"Число B: {threshold}")
    
    count, product = find_elements_greater_than(array, threshold)
    
    print(f"Результат:")
    print(f"  Количество элементов > {threshold}: {count}")
    print(f"  Произведение: {product}")
    print()

def example_4():
    """
    Пример 4: Отрицательные числа
    """
    print("ПРИМЕР 4: Отрицательные числа")
    print("-" * 40)
    
    array = [-5, -2, 0, 3, 7, -1]
    threshold = -3
    
    print(f"Массив: {array}")
    print(f"Число B: {threshold}")
    
    count, product = find_elements_greater_than(array, threshold)
    
    print(f"Результат:")
    print(f"  Количество элементов > {threshold}: {count}")
    print(f"  Произведение: {product}")
    print()

def example_5():
    """
    Пример 5: Дробные числа
    """
    print("ПРИМЕР 5: Дробные числа")
    print("-" * 40)
    
    array = [1.5, 2.7, 3.2, 4.1, 2.0]
    threshold = 2.5
    
    print(f"Массив: {array}")
    print(f"Число B: {threshold}")
    
    count, product = find_elements_greater_than(array, threshold)
    
    print(f"Результат:")
    print(f"  Количество элементов > {threshold}: {count}")
    print(f"  Произведение: {product}")
    print()

def example_6():
    """
    Пример 6: Пустой массив
    """
    print("ПРИМЕР 6: Пустой массив")
    print("-" * 40)
    
    array = []
    threshold = 5
    
    print(f"Массив: {array}")
    print(f"Число B: {threshold}")
    
    count, product = find_elements_greater_than(array, threshold)
    
    print(f"Результат:")
    print(f"  Количество элементов > {threshold}: {count}")
    print(f"  Произведение: {product}")
    print()

def main():
    """
    Запуск всех примеров
    """
    print("ПРИМЕРЫ ИСПОЛЬЗОВАНИЯ ПРОГРАММЫ")
    print("=" * 50)
    print()
    
    example_1()
    example_2()
    example_3()
    example_4()
    example_5()
    example_6()
    
    print("=" * 50)
    print("ВСЕ ПРИМЕРЫ ЗАВЕРШЕНЫ")

if __name__ == "__main__":
    main() 