'''
#Задание Дано множество A из N точек (N > 2, точки заданы своими координатами x, y). 
# Найти такую точку из данного множества, сумма расстояний от которой до остальных его точек минимальна, и саму эту сумму.
Расстояние R между точками с координатами (x1, y1) и (x2, y2) вычисляется по формуле:
sqrt((x2-x1)**2 + (y2-y1)**2)
Для хранения данных о каждом наборе точек следует использовать по два списка: первый список для хранения абсцисс, 
второй — для хранения ординат.
'''
import math
import random

try:
    N = random.randint(3, 10) 
    print(f"Количество точек N = {N}")
    
    x_coords = []
    y_coords = []
    
    for i in range(N):
        x_coords.append(random.randint(-10, 10))
        y_coords.append(random.randint(-10, 10))
    
    print(f"Координаты X: {x_coords}")
    print(f"Координаты Y: {y_coords}")
    
    min_sum = float('inf')
    min_point_index = -1
    
    for i in range(N):
        current_sum = 0
        x1 = x_coords[i]
        y1 = y_coords[i]
       
        for j in range(N):
            if i != j:
                x2 = x_coords[j]
                y2 = y_coords[j]
                distance = math.sqrt((x2 - x1)**2 + (y2 - y1)**2)
                current_sum += distance
        
        if current_sum < min_sum:
            min_sum = current_sum
            min_point_index = i
            
    print(f"\nТочка с минимальной суммой расстояний:")
    print(f"Индекс: {min_point_index}")
    print(f"Координаты: ({x_coords[min_point_index]}, {y_coords[min_point_index]})")
    print(f"Сумма расстояний до остальных точек: {int(min_sum)}")

except ValueError:
    print("Ошибка")
