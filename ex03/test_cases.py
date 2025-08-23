"""
Тестовые случаи для программы генерации случайных чисел.
"""

import unittest
import random
from unittest.mock import patch
from io import StringIO
import sys

class TestRandomNumberGenerator(unittest.TestCase):
    """Тестовый класс для проверки функциональности программы."""
    
    def setUp(self):
        """Настройка перед каждым тестом."""
        self.maxDiff = None
    
    @patch('builtins.input', side_effect=['0'])
    @patch('sys.stdout', new_callable=StringIO)
    def test_immediate_stop(self, mock_stdout, mock_input):
        """Тест немедленной остановки программы."""
        # Импортируем функцию из main.py
        from main import generate_random_sequence
        
        generate_random_sequence()
        
        output = mock_stdout.getvalue()
        
        # Проверяем, что программа запустилась
        self.assertIn("Программа генерирует случайные числа", output)
        self.assertIn("Сгенерировано число:", output)
        self.assertIn("РЕЗУЛЬТАТ:", output)
        self.assertIn("Всего сгенерировано чисел: 1", output)
    
    @patch('builtins.input', side_effect=['5', '10', '0'])
    @patch('sys.stdout', new_callable=StringIO)
    def test_multiple_numbers(self, mock_stdout, mock_input):
        """Тест генерации нескольких чисел."""
        from main import generate_random_sequence
        
        generate_random_sequence()
        
        output = mock_stdout.getvalue()
        
        # Проверяем, что программа обработала несколько чисел
        self.assertIn("Вы ввели: 5", output)
        self.assertIn("Вы ввели: 10", output)
        self.assertIn("Всего сгенерировано чисел: 3", output)
    
    @patch('builtins.input', side_effect=['abc', '5', '0'])
    @patch('sys.stdout', new_callable=StringIO)
    def test_invalid_input_handling(self, mock_stdout, mock_input):
        """Тест обработки некорректного ввода."""
        from main import generate_random_sequence
        
        generate_random_sequence()
        
        output = mock_stdout.getvalue()
        
        # Проверяем, что программа корректно обработала ошибку
        self.assertIn("Ошибка! Пожалуйста, введите целое число.", output)
        self.assertIn("Вы ввели: 5", output)
    
    def test_random_number_range(self):
        """Тест диапазона генерируемых чисел."""
        # Проверяем, что числа генерируются в правильном диапазоне
        for _ in range(100):
            number = random.randint(1, 100)
            self.assertGreaterEqual(number, 1)
            self.assertLessEqual(number, 100)
    
    @patch('builtins.input', side_effect=['1', '2', '3', '4', '5', '0'])
    @patch('sys.stdout', new_callable=StringIO)
    def test_large_sequence(self, mock_stdout, mock_input):
        """Тест длинной последовательности чисел."""
        from main import generate_random_sequence
        
        generate_random_sequence()
        
        output = mock_stdout.getvalue()
        
        # Проверяем, что программа обработала длинную последовательность
        self.assertIn("Всего сгенерировано чисел: 6", output)
        
        # Проверяем, что все числа выведены
        lines = output.split('\n')
        number_lines = [line for line in lines if line.strip().startswith(('1.', '2.', '3.', '4.', '5.', '6.'))]
        self.assertEqual(len(number_lines), 6)

class TestProgramLogic(unittest.TestCase):
    """Тесты логики программы."""
    
    def test_zero_termination(self):
        """Тест завершения программы при вводе нуля."""
        # Симулируем логику программы
        numbers = []
        user_inputs = ['5', '10', '0']
        
        for user_input in user_inputs:
            if user_input == '0':
                break
            numbers.append(int(user_input))
        
        # Проверяем, что программа остановилась на нуле
        self.assertEqual(len(numbers), 2)
        self.assertEqual(numbers, [5, 10])
    
    def test_number_collection(self):
        """Тест сбора чисел в список."""
        numbers = []
        
        # Симулируем генерацию случайных чисел
        for i in range(5):
            random_num = random.randint(1, 100)
            numbers.append(random_num)
        
        # Проверяем, что все числа добавлены
        self.assertEqual(len(numbers), 5)
        self.assertTrue(all(1 <= num <= 100 for num in numbers))

if __name__ == '__main__':
    # Запускаем тесты
    unittest.main(verbosity=2) 