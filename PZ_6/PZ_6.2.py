"""
Дано число R и список A размера N. Найти элемент списка, который наиболее близок
к числу R (то есть такой элемент AK, для которого величина |AK - R| является
минимальной).
"""
import random
R = int(input("Введите число R: "))
N = int(input("Введите длину списка: "))
A = [random.randint(0, 101) for _ in range(N)]

best_elem = A[0]
best_diff = (A[0] - R) 

for i in range(1, N):
    current_diff = (A[i] - R)  
    if current_diff < best_diff:  
        best_diff = current_diff  
        best_elem = A[i]          
print("Элемент, наиболее близкий к R:", best_elem)
print(A)


