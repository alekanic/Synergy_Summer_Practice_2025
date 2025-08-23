#!/usr/bin/env python3
# -*- coding: utf-8 -*-

def analyze_matrix(matrix):
    """
    Анализирует матрицу и находит сумму элементов главной диагонали
    и количество положительных элементов.
    """
    if not matrix or not matrix[0]:
        return 0, 0
    
    rows = len(matrix)
    cols = len(matrix[0])
    
    # Сумма элементов главной диагонали
    diagonal_sum = 0
    min_dim = min(rows, cols)
    for i in range(min_dim):
        diagonal_sum += matrix[i][i]
    
    # Количество положительных элементов
    positive_count = 0
    for row in matrix:
        for element in row:
            if element > 0:
                positive_count += 1
    
    return diagonal_sum, positive_count


def input_matrix():
    """
    Вводит матрицу с клавиатуры.
    """
    try:
        n = int(input("Введите количество строк N: "))
        m = int(input("Введите количество столбцов M: "))
        
        if n <= 0 or m <= 0:
            print("Ошибка: размеры матрицы должны быть положительными числами!")
            return []
        
        print(f"Введите элементы матрицы {n}×{m}:")
        matrix = []
        
        for i in range(n):
            row = []
            for j in range(m):
                element = float(input(f"Элемент [{i+1}][{j+1}]: "))
                row.append(element)
            matrix.append(row)
        
        return matrix
    
    except ValueError:
        print("Ошибка: введите корректное числовое значение!")
        return []


def display_matrix(matrix):
    """
    Выводит матрицу в красивом формате.
    """
    if not matrix:
        print("Матрица пуста.")
        return
    
    print("\nМатрица:")
    for row in matrix:
        print(" ".join(f"{element:8.2f}" for element in row))


def display_results(matrix, diagonal_sum, positive_count):
    """
    Выводит результаты анализа матрицы.
    """
    print("\n" + "="*50)
    print("РЕЗУЛЬТАТЫ АНАЛИЗА МАТРИЦЫ")
    print("="*50)
    
    display_matrix(matrix)
    
    print(f"\nРазмер матрицы: {len(matrix)}×{len(matrix[0]) if matrix else 0}")
    print(f"Сумма элементов главной диагонали: {diagonal_sum}")
    print(f"Количество положительных элементов: {positive_count}")
    
    if matrix:
        total_elements = len(matrix) * len(matrix[0])
        positive_percentage = (positive_count / total_elements) * 100
        print(f"Процент положительных элементов: {positive_percentage:.1f}%")
    
    print("="*50)


def main():
    """
    Основная функция программы.
    """
    print("АНАЛИЗ МАТРИЦЫ")
    print("Поиск суммы элементов главной диагонали и количества положительных элементов")
    print("-" * 50)
    
    # Ввод матрицы
    matrix = input_matrix()
    
    if not matrix:
        print("Программа завершена из-за ошибки ввода.")
        return
    
    # Анализ матрицы
    diagonal_sum, positive_count = analyze_matrix(matrix)
    
    # Вывод результатов
    display_results(matrix, diagonal_sum, positive_count)


if __name__ == "__main__":
    main() 