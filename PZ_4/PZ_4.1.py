# Дано целое число N (> 0). Найти сумму N2 + (N + 1)2 + (N + 2)2 + ... + (2N)2
try:  
  N = int(input("Введите целое число N (> 0): "))
  if N <= 0:
    print("N должно быть больше 0.")
  else:
      summa = 0
      for i in range(N, 2 * N + 1):
          summa += i**2 
      print("Сумма квадратов:", summa)
except ValueError:
   print("Введите целое число")


