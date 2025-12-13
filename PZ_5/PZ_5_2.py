'''
#Задание Описать функцию InvertDigits(K), меняющую порядок следования цифр целого положительного числа K на обратный
 (K — параметр целого типа, являющийся одновременно входным и выходным). 
 С помощью этой функции поменять порядок следования цифр на обратный для каждого из пяти данных целых чисел.
'''
def InvertDigits(K):
    reversed_num = 0
    temp = K
 
    while temp > 0:
        last_digit = temp % 10
        reversed_num = reversed_num * 10 + last_digit
        temp = temp // 10
    
    return reversed_num


print("Введите 5 целых положительных чисел:")

count = 1
while count <= 5:
    try:
        num = int(input(f"Число {count}: "))
        
        if num > 0:
            # Вызов функции
            result = InvertDigits(num)
            print(f"Исходное: {num}, Обратное: {result}")
            count += 1
        else:
            print("Число должно быть положительным! Попробуйте снова.")
            
    except:
        print("Ошибка ввода! Введите целое число.")

print("Обработка завершена.")
