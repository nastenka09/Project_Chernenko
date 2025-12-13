'''
Задание: Составить программу, в которой функция построит изображение, 
в котором в первой строке 1 звездочка, во второй - 2, в третьей - 3, ...,
 в строке с номером m - m звездочек.
'''
try:
    def PaintStars(m):
        row = 1
        while row <= m:
            stars = 1
            while stars <= row: 
                print("*", end="")
                stars += 1
            print() 
            row += 1

    a = int(input('Введите количество строк: '))
    PaintStars(a)
except ValueError:
    print('Ошибка! Введите число')
