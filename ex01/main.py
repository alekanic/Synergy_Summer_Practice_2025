#!/usr/bin/env python3
# -*- coding: utf-8 -*-

def analyze_positive_elements(arr):

    sum_positive = 0
    count_positive = 0
    
    for element in arr:
        if element > 0:
            sum_positive += element
            count_positive += 1
    
    return sum_positive, count_positive


def input_array():

    try:
        n = int(input("Введите размерность массива N: "))
        if n <= 0:
            print("Ошибка: размерность должна быть положительным числом!")
            return []
        
        print(f"Введите {n} элементов массива:")
        arr = []
        for i in range(n):
            element = float(input(f"Элемент {i+1}: "))
            arr.append(element)
        
        return arr
    
    except ValueError:
        print("Ошибка: введите корректное числовое значение!")
        return []


def display_results(arr, sum_positive, count_positive):
    
    print("\n" + "="*50)
    print("РЕЗУЛЬТАТЫ АНАЛИЗА МАССИВА")
    print("="*50)
    print(f"Исходный массив: {arr}")
    print(f"Размерность массива: {len(arr)}")
    print(f"Количество положительных элементов: {count_positive}")
    print(f"Сумма положительных элементов: {sum_positive}")
    
    if count_positive > 0:
        average = sum_positive / count_positive
        print(f"Среднее значение положительных элементов: {average:.2f}")
    else:
        print("Положительных элементов не найдено.")
    print("="*50)


def main():

    print("АНАЛИЗ ОДНОМЕРНОГО МАССИВА")
    print("Поиск суммы положительных элементов и их количества")
    print("-" * 50)
    
    # Ввод массива
    arr = input_array()
    
    if not arr:
        print("Программа завершена из-за ошибки ввода.")
        return
    
    # Анализ массива
    sum_positive, count_positive = analyze_positive_elements(arr)
    
    # Вывод результатов
    display_results(arr, sum_positive, count_positive)


if __name__ == "__main__":
    main() 


