# Задайте число. Составьте список чисел Фибоначчи, в том числе для отрицательных индексов.

fib1 = 1
fib2 = 1
 
num = int(input("Номер элемента ряда Фибоначчи: "))
 
i = 0
while i < num - 2:
    fib_sum = fib1 + fib2
    fib1 = fib2
    fib2 = fib_sum
    i += 1
    print(fib2, end=' ')
print()

# fib3 = 1
# fib4 = -1
 
# m = int(input("Номер элемента ряда НегаФибоначчи: "))
 
# j = 0
# while j < m + 2:
#     fib1_sum = fib4 - fib3
#     fib3 = fib4
#     fib4 = fib1_sum
#     j = j + 1
#     print(fib4, end=' ')