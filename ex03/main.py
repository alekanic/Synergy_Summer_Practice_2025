import random

def generate_random_sequence():
    """
    Генерирует последовательность случайных чисел до тех пор, 
    пока пользователь не введёт ноль.
    Выводит все числа, кроме последнего (нуля).
    """
    numbers = []
    
    print("Программа генерирует последовательность случайных чисел.")
    print("Введите 0, чтобы остановить генерацию.")
    print("-" * 40)
    
    while True:
        # Генерируем случайное число от 1 до 100
        random_number = random.randint(1, 100)
        numbers.append(random_number)
        
        # Запрашиваем у пользователя ввод
        try:
            user_input = input("Введите число (0 для остановки): ")
            user_number = int(user_input)
            
            if user_number == 0:
                break
                
        except ValueError:
            print("Ошибка! Пожалуйста, введите целое число.")
            continue
    
    print("\n" + "=" * 40)
    print("РЕЗУЛЬТАТ:")
    print("Все сгенерированные числа (кроме последнего):")
    
    # Выводим все числа, кроме последнего (нуля)
    if numbers:
        for i, num in enumerate(numbers, 1):
            print(f"{i}. {num}")
    
    print(f"\nВсего сгенерировано чисел: {len(numbers)}")

if __name__ == "__main__":
    generate_random_sequence() 

    