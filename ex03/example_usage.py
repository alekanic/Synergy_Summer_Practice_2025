"""
Пример использования программы генерации последовательности случайных чисел.
Этот файл демонстрирует, как работает основная программа.
"""

import random
from io import StringIO
import sys

def simulate_program_run():
    """
    Симулирует работу программы с предопределенными входами
    для демонстрации функциональности.
    """
    print("ДЕМОНСТРАЦИЯ РАБОТЫ ПРОГРАММЫ")
    print("=" * 50)
    
    # Симулируем ввод пользователя
    test_inputs = ["5", "10", "0"]  # Пользователь вводит 5, затем 10, затем 0
    
    numbers = []
    input_index = 0
    
    print("Программа генерирует последовательность случайных чисел.")
    print("Введите 0, чтобы остановить генерацию.")
    print("-" * 40)
    
    while True:
        # Генерируем случайное число от 1 до 100
        random_number = random.randint(1, 100)
        numbers.append(random_number)
        
        # Симулируем ввод пользователя
        if input_index < len(test_inputs):
            user_input = test_inputs[input_index]
            input_index += 1
            print(f"Введите число (0 для остановки): {user_input}")
            
            try:
                user_number = int(user_input)
                
                if user_number == 0:
                    break
                    
            except ValueError:
                print("Ошибка! Пожалуйста, введите целое число.")
                continue
        else:
            break
    
    print("\n" + "=" * 40)
    print("РЕЗУЛЬТАТ:")
    print("Все сгенерированные числа (кроме последнего):")
    
    # Выводим все числа, кроме последнего (нуля)
    if numbers:
        for i, num in enumerate(numbers, 1):
            print(f"{i}. {num}")
    
    print(f"\nВсего сгенерировано чисел: {len(numbers)}")

def test_edge_cases():
    """
    Тестирует граничные случаи программы.
    """
    print("\n\nТЕСТИРОВАНИЕ ГРАНИЧНЫХ СЛУЧАЕВ")
    print("=" * 50)
    
    # Тест 1: Немедленная остановка
    print("Тест 1: Немедленная остановка (ввод 0 сразу)")
    numbers = []
    random_number = random.randint(1, 100)
    numbers.append(random_number)
    print(f"Сгенерировано число: {random_number}")
    print("Ввод: 0")
    print("Результат: Программа остановилась после первого числа")
    print(f"Последовательность: {numbers}")
    
    # Тест 2: Множественные числа
    print("\nТест 2: Множественные числа")
    numbers = [random.randint(1, 100) for _ in range(5)]
    print(f"Сгенерированная последовательность: {numbers}")
    print("Ввод: 0")
    print("Результат: Выводятся все числа кроме последнего")
    print(f"Выводимые числа: {numbers}")

def demonstrate_sequence_generation():
    """
    Демонстрирует процесс генерации последовательности.
    """
    print("\n\nДЕМОНСТРАЦИЯ ГЕНЕРАЦИИ ПОСЛЕДОВАТЕЛЬНОСТИ")
    print("=" * 50)
    
    print("Процесс генерации последовательности:")
    numbers = []
    
    for i in range(5):
        random_number = random.randint(1, 100)
        numbers.append(random_number)
        print(f"Итерация {i+1}: Добавлено число {random_number}")
        print(f"Текущая последовательность: {numbers}")
    
    print(f"\nИтоговая последовательность: {numbers}")
    print("При вводе 0 программа выведет все числа из этой последовательности")

if __name__ == "__main__":
    simulate_program_run()
    test_edge_cases()
    demonstrate_sequence_generation() 