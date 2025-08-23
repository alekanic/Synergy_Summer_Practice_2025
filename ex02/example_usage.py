#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from main import analyze_matrix, display_matrix, display_results


def example_1():
    """Пример 1: Квадратная матрица 3x3."""
    print("ПРИМЕР 1: Квадратная матрица 3x3")
    print("-" * 40)
    
    matrix = [
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9]
    ]
    
    diagonal_sum, positive_count = analyze_matrix(matrix)
    display_results(matrix, diagonal_sum, positive_count)


def example_2():
    """Пример 2: Прямоугольная матрица 2x4."""
    print("\nПРИМЕР 2: Прямоугольная матрица 2x4")
    print("-" * 40)
    
    matrix = [
        [1, 2, 3, 4],
        [5, 6, 7, 8]
    ]
    
    diagonal_sum, positive_count = analyze_matrix(matrix)
    display_results(matrix, diagonal_sum, positive_count)


def example_3():
    """Пример 3: Матрица с отрицательными элементами."""
    print("\nПРИМЕР 3: Матрица с отрицательными элементами")
    print("-" * 40)
    
    matrix = [
        [1, -2, 3],
        [-4, 5, -6],
        [7, -8, 9]
    ]
    
    diagonal_sum, positive_count = analyze_matrix(matrix)
    display_results(matrix, diagonal_sum, positive_count)


def example_4():
    """Пример 4: Матрица с нулевыми элементами."""
    print("\nПРИМЕР 4: Матрица с нулевыми элементами")
    print("-" * 40)
    
    matrix = [
        [0, 1, 0],
        [1, 0, 1],
        [0, 1, 0]
    ]
    
    diagonal_sum, positive_count = analyze_matrix(matrix)
    display_results(matrix, diagonal_sum, positive_count)


def example_5():
    """Пример 5: Матрица с одним элементом."""
    print("\nПРИМЕР 5: Матрица с одним элементом")
    print("-" * 40)
    
    matrix = [[5]]
    
    diagonal_sum, positive_count = analyze_matrix(matrix)
    display_results(matrix, diagonal_sum, positive_count)


def example_6():
    """Пример 6: Большая матрица 5x5."""
    print("\nПРИМЕР 6: Большая матрица 5x5")
    print("-" * 40)
    
    matrix = [
        [1, 2, 3, 4, 5],
        [6, 7, 8, 9, 10],
        [11, 12, 13, 14, 15],
        [16, 17, 18, 19, 20],
        [21, 22, 23, 24, 25]
    ]
    
    diagonal_sum, positive_count = analyze_matrix(matrix)
    display_results(matrix, diagonal_sum, positive_count)


def example_7():
    """Пример 7: Матрица со всеми отрицательными элементами."""
    print("\nПРИМЕР 7: Матрица со всеми отрицательными элементами")
    print("-" * 40)
    
    matrix = [
        [-1, -2, -3],
        [-4, -5, -6],
        [-7, -8, -9]
    ]
    
    diagonal_sum, positive_count = analyze_matrix(matrix)
    display_results(matrix, diagonal_sum, positive_count)


def example_8():
    """Пример 8: Широкая матрица (больше столбцов, чем строк)."""
    print("\nПРИМЕР 8: Широкая матрица 2x5")
    print("-" * 40)
    
    matrix = [
        [1, 2, 3, 4, 5],
        [6, 7, 8, 9, 10]
    ]
    
    diagonal_sum, positive_count = analyze_matrix(matrix)
    display_results(matrix, diagonal_sum, positive_count)


def example_9():
    """Пример 9: Высокая матрица (больше строк, чем столбцов)."""
    print("\nПРИМЕР 9: Высокая матрица 4x2")
    print("-" * 40)
    
    matrix = [
        [1, 2],
        [3, 4],
        [5, 6],
        [7, 8]
    ]
    
    diagonal_sum, positive_count = analyze_matrix(matrix)
    display_results(matrix, diagonal_sum, positive_count)


def example_10():
    """Пример 10: Пустая матрица."""
    print("\nПРИМЕР 10: Пустая матрица")
    print("-" * 40)
    
    matrix = []
    
    diagonal_sum, positive_count = analyze_matrix(matrix)
    display_results(matrix, diagonal_sum, positive_count)


def main():
    """Основная функция для запуска примеров."""
    print("ПРИМЕРЫ ИСПОЛЬЗОВАНИЯ ПРОГРАММЫ АНАЛИЗА МАТРИЦ")
    print("=" * 60)
    
    examples = [
        example_1,
        example_2,
        example_3,
        example_4,
        example_5,
        example_6,
        example_7,
        example_8,
        example_9,
        example_10
    ]
    
    for i, example_func in enumerate(examples, 1):
        try:
            example_func()
        except Exception as e:
            print(f"Ошибка в примере {i}: {e}")
        
        if i < len(examples):
            print("\n" + "="*60)
    
    print("\n" + "="*60)
    print("ВСЕ ПРИМЕРЫ ЗАВЕРШЕНЫ")


if __name__ == "__main__":
    main() 