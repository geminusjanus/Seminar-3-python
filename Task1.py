# Задайте список из нескольких чисел. 
# Напишите программу, которая найдёт сумму элементов списка, стоящих на нечётной позиции.

# Пример:

# - [2, 3, 5, 9, 3] -> на нечётных позициях элементы 3 и 9, ответ: 12

myList = [1, 2, 3, 4, 5, 6, 7, 8, 9]
print("Список чисел:")
print(myList)
list_length = len(myList)
sumOfElements = 0
for i in range(list_length):
    if i % 2 != 0:
        sumOfElements += myList[i]
print("Сумма чисел на нечетных позициях:", sumOfElements)