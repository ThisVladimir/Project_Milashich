try:
    segment1 = int(input("Введите длину первого отрезка:"))
    segment2 = int(input("Введите длину второго отрезка(меньше первого отрезка):"))
    remainder = segment1 % segment2
    print("Незанятая часть отрезка А:",remainder)
except ValueError:
    print("Неправильный ввод данных. Введите число.")