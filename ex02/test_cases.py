#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import unittest
from main import analyze_matrix


class TestMatrixAnalysis(unittest.TestCase):
    """Тестовый класс для проверки функциональности программы."""
    
    def test_square_matrix(self):
        """Тест квадратной матрицы."""
        matrix = [
            [1, 2, 3],
            [4, 5, 6],
            [7, 8, 9]
        ]
        diagonal_sum, positive_count = analyze_matrix(matrix)
        
        # Сумма главной диагонали: 1 + 5 + 9 = 15
        self.assertEqual(diagonal_sum, 15)
        # Количество положительных элементов: 9
        self.assertEqual(positive_count, 9)
    
    def test_rectangular_matrix(self):
        """Тест прямоугольной матрицы."""
        matrix = [
            [1, 2, 3, 4],
            [5, 6, 7, 8]
        ]
        diagonal_sum, positive_count = analyze_matrix(matrix)
        
        # Сумма главной диагонали: 1 + 6 = 7 (минимальная размерность 2)
        self.assertEqual(diagonal_sum, 7)
        # Количество положительных элементов: 8
        self.assertEqual(positive_count, 8)
    
    def test_matrix_with_negative_elements(self):
        """Тест матрицы с отрицательными элементами."""
        matrix = [
            [1, -2, 3],
            [-4, 5, -6],
            [7, -8, 9]
        ]
        diagonal_sum, positive_count = analyze_matrix(matrix)
        
        # Сумма главной диагонали: 1 + 5 + 9 = 15
        self.assertEqual(diagonal_sum, 15)
        # Количество положительных элементов: 5 (1, 3, 5, 7, 9)
        self.assertEqual(positive_count, 5)
    
    def test_matrix_with_zeros(self):
        """Тест матрицы с нулевыми элементами."""
        matrix = [
            [0, 1, 0],
            [1, 0, 1],
            [0, 1, 0]
        ]
        diagonal_sum, positive_count = analyze_matrix(matrix)
        
        # Сумма главной диагонали: 0 + 0 + 0 = 0
        self.assertEqual(diagonal_sum, 0)
        # Количество положительных элементов: 4 (единицы)
        self.assertEqual(positive_count, 4)
    
    def test_empty_matrix(self):
        """Тест пустой матрицы."""
        matrix = []
        diagonal_sum, positive_count = analyze_matrix(matrix)
        
        self.assertEqual(diagonal_sum, 0)
        self.assertEqual(positive_count, 0)
    
    def test_single_element_matrix(self):
        """Тест матрицы с одним элементом."""
        matrix = [[5]]
        diagonal_sum, positive_count = analyze_matrix(matrix)
        
        self.assertEqual(diagonal_sum, 5)
        self.assertEqual(positive_count, 1)
    
    def test_large_matrix(self):
        """Тест большой матрицы."""
        matrix = [
            [1, 2, 3, 4, 5],
            [6, 7, 8, 9, 10],
            [11, 12, 13, 14, 15],
            [16, 17, 18, 19, 20],
            [21, 22, 23, 24, 25]
        ]
        diagonal_sum, positive_count = analyze_matrix(matrix)
        
        # Сумма главной диагонали: 1 + 7 + 13 + 19 + 25 = 65
        self.assertEqual(diagonal_sum, 65)
        # Количество положительных элементов: 25
        self.assertEqual(positive_count, 25)
    
    def test_matrix_with_all_negative(self):
        """Тест матрицы со всеми отрицательными элементами."""
        matrix = [
            [-1, -2, -3],
            [-4, -5, -6],
            [-7, -8, -9]
        ]
        diagonal_sum, positive_count = analyze_matrix(matrix)
        
        # Сумма главной диагонали: -1 + (-5) + (-9) = -15
        self.assertEqual(diagonal_sum, -15)
        # Количество положительных элементов: 0
        self.assertEqual(positive_count, 0)


class TestMatrixEdgeCases(unittest.TestCase):
    """Тесты граничных случаев."""
    
    def test_wide_matrix(self):
        """Тест широкой матрицы (больше столбцов, чем строк)."""
        matrix = [
            [1, 2, 3, 4, 5],
            [6, 7, 8, 9, 10]
        ]
        diagonal_sum, positive_count = analyze_matrix(matrix)
        
        # Сумма главной диагонали: 1 + 7 = 8 (минимальная размерность 2)
        self.assertEqual(diagonal_sum, 8)
        self.assertEqual(positive_count, 10)
    
    def test_tall_matrix(self):
        """Тест высокой матрицы (больше строк, чем столбцов)."""
        matrix = [
            [1, 2],
            [3, 4],
            [5, 6],
            [7, 8]
        ]
        diagonal_sum, positive_count = analyze_matrix(matrix)
        
        # Сумма главной диагонали: 1 + 4 = 5 (минимальная размерность 2)
        self.assertEqual(diagonal_sum, 5)
        self.assertEqual(positive_count, 8)


def run_test_case(test_name, matrix, expected_diagonal, expected_positive):
    """Запускает тестовый случай и выводит результат."""
    print(f"\nТест: {test_name}")
    print(f"Матрица: {matrix}")
    
    diagonal_sum, positive_count = analyze_matrix(matrix)
    
    print(f"Ожидаемая сумма диагонали: {expected_diagonal}, получено: {diagonal_sum}")
    print(f"Ожидаемое количество положительных: {expected_positive}, получено: {positive_count}")
    
    if diagonal_sum == expected_diagonal and positive_count == expected_positive:
        print("✅ ТЕСТ ПРОЙДЕН")
        return True
    else:
        print("❌ ТЕСТ НЕ ПРОЙДЕН")
        return False


def main():
    """Основная функция для запуска тестов."""
    print("ТЕСТИРОВАНИЕ ПРОГРАММЫ АНАЛИЗА МАТРИЦ")
    print("=" * 50)
    
    # Тестовые случаи
    test_cases = [
        ("Квадратная матрица 3x3", 
         [[1, 2, 3], [4, 5, 6], [7, 8, 9]], 15, 9),
        
        ("Прямоугольная матрица 2x4", 
         [[1, 2, 3, 4], [5, 6, 7, 8]], 7, 8),
        
        ("Матрица с отрицательными элементами", 
         [[1, -2, 3], [-4, 5, -6], [7, -8, 9]], 15, 5),
        
        ("Матрица с нулями", 
         [[0, 1, 0], [1, 0, 1], [0, 1, 0]], 0, 4),
        
        ("Один элемент", 
         [[5]], 5, 1),
        
        ("Все отрицательные", 
         [[-1, -2], [-3, -4]], -5, 0)
    ]
    
    passed = 0
    total = len(test_cases)
    
    for test_name, matrix, expected_diagonal, expected_positive in test_cases:
        if run_test_case(test_name, matrix, expected_diagonal, expected_positive):
            passed += 1
    
    print(f"\n{'='*50}")
    print(f"РЕЗУЛЬТАТЫ ТЕСТИРОВАНИЯ: {passed}/{total} тестов пройдено")
    
    if passed == total:
        print("🎉 ВСЕ ТЕСТЫ ПРОЙДЕНЫ УСПЕШНО!")
    else:
        print("⚠️  НЕКОТОРЫЕ ТЕСТЫ НЕ ПРОЙДЕНЫ")


if __name__ == "__main__":
    main() 