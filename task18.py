"""Задача 18: Требуется найти в массиве A[1..N] самый близкий по величине элемент к заданному числу X. Пользователь в первой строке вводит натуральное число N – количество элементов в массиве. В последующих  строках записаны N целых чисел Ai. Последняя строка содержит число X

*Пример:*

5
    1 2 3 4 5
    6
    -> 5
    """
import random
source=[0]*4
for i in range(len(source)):
    source[i]=random.randrange(1,25)
print(source)

index=0
numb=int(input("number: "))

min = abs(numb - source[0])
for j in range(len(source)):
    temp = abs(numb-source[j])
    if temp<min:
        min = temp
        index=j
print(source[index])
