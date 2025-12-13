'''
#Задание Дан список ненулевых целых чисел размера N. Проверить, чередуются ли в нем положительные и отрицательные числа.
 Если чередуются, то вывести 0, если нет, то вывести порядковый номер первого элемента, нарушающего закономерность.
'''
import random

try:
    N = random.randint(1, 10)
    numbers = []
    for _ in range(N):
        num = random.randint(-100, 100)
        if num != 0:
            numbers.append(num)
    result = 0
    for i in range(1, N):
        if numbers[i-1] * numbers[i] > 0:
            result = i + 1  
    
    print(f"Сгенерированный список: {numbers}")
    print(f"Результат: {result}")
    
except ValueError:
    print("Ошибко")
