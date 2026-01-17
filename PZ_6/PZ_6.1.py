"""
Дан список A размера N и целое число K (1 < K < N). Вывести элементы список с
порядковыми номерами, кратными K: AK, A2*K, A3*K,... . Условный оператор не
использовать.
"""
import random
N = int(input("Введите длину списка: "))
A = [random.randint(1, 101) for _ in range(N)]

K = int(input("Введите число: "))
B = []
for i in range(K - 1, N, K):
    B.append(A[i])

print(B)
print(A)