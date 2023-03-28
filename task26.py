"""
Задача 26:  Напишите программу, которая на вход принимает два числа A и B, и возводит число А в целую степень B с помощью рекурсии.
"""

def value_numb(a,b):
    if b <= 0:
        return 1
    return a*value_numb(a,b-1) 
a = int(input("Введите число: "))
b = int(input("Введите степень: "))
print(value_numb(a,b))

#upd