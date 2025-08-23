#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Программа для поиска количества элементов, больших заданного числа В,
и их произведения в одномерном массиве А размерности N.

Автор: Практика
Дата: 2024
"""

def input_array():

    while True:
        try:
            n = int(input("Введите размерность массива N: "))
            if n <= 0:
                print("Размерность должна быть положительным числом!")
                continue
            break
        except ValueError:
            print("Ошибка! Введите целое число.")
    
    array = []
    print(f"Введите {n} элементов массива:")
    
    for i in range(n):
        while True:
            try:
                element = float(input(f"Элемент {i+1}: "))
                array.append(element)
                break
            except ValueError:
                print("Ошибка! Введите число.")
    
    return array

def input_threshold():

    while True:
        try:
            b = float(input("Введите число B для сравнения: "))
            return b
        except ValueError:
            print("Ошибка! Введите число.")

def find_elements_greater_than(array, threshold):
    
    count = 0
    product = 1
    
    for element in array:
        if element > threshold:
            count += 1
            product *= element
    
    return count, product

def main():

    print("=" * 50)
    print("ПРОГРАММА ДЛЯ ПОИСКА ЭЛЕМЕНТОВ БОЛЬШЕ ЗАДАННОГО ЧИСЛА")
    print("=" * 50)
    
    # Ввод данных
    array = input_array()
    threshold = input_threshold()
    
    print("\n" + "=" * 50)
    print("ИСХОДНЫЕ ДАННЫЕ:")
    print(f"Массив A: {array}")
    print(f"Число B: {threshold}")
    print("=" * 50)
    
    # Вычисление результата
    count, product = find_elements_greater_than(array, threshold)
    
    # Вывод результатов
    print("\nРЕЗУЛЬТАТЫ:")
    print(f"Количество элементов больше {threshold}: {count}")
    
    if count > 0:
        print(f"Произведение элементов больше {threshold}: {product}")
    else:
        print("Элементов больше заданного числа не найдено.")
    
    print("=" * 50)

if __name__ == "__main__":
    main() 