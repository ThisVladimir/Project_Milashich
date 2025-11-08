"""
Составить функцию решения задачи: из заданного числа вычли сумму его цифр. Из
результата вновь вычли сумму его цифр и т. д. Через сколько таких действий
получится нуль?
"""
def sum_digits(x):
    s = 0
    while x > 0:
        s += x % 10  
        x //= 10     
    return s
def steps_to_zero(n):
    steps = 0
    while n > 0:
        n -= sum_digits(n)  
        steps += 1          
    return steps

number = int(input("Введите число: "))
result = steps_to_zero(number)
print(f"Чтобы получить ноль, нужно {steps_to_zero(number)} шаг(ов).")

