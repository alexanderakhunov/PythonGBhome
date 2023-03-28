"""
Задача 22: Даны два неупорядоченных набора целых чисел (может быть, с повторениями). Выдать без повторений в порядке возрастания все те числа, которые встречаются в обоих наборах.
Пользователь вводит 2 числа. n - кол-во элементов первого множества. m - кол-во элементов второго множества. Затем пользователь вводит сами элементы множеств.
"""
import random
list1=[0]*50
list2=[0]*50

def pool_list(list):
    for i in range(len(list)):
        list[i]=random.randint(0,25)
    return list

print(pool_list(list1))
print(pool_list(list2))
set1=set(list1)
set2=set(list2)
print(sorted(set1.intersection(set2)))
