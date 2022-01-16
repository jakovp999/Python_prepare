# найти одинаковые фрукты в двух списках
# первый способ
import math

# basket = ['apple', 'pear', 'plum', 'mango', 'dragon-fruit', 'durian', 'kiwi', 'pinapple']
# fridge = ['pear', 'orange', 'grape', 'kumkwat', 'mango', 'pinapple', 'lichi', 'passion-fruit']
#
# result = []
#
# for fruit in basket:
#     if fruit in fridge:
#         result.append(fruit)
#
# print(result)
# print(type(result))
# #  Второй способ
#
# result = [fruit for fruit in basket if fruit in fridge]
#
# print(result)
#
#
# # Найти элемент кратен 3, элемент положительный, элемент не кратен 4
# numlist = [18, -32, 57, -7, 0, 72, 10, 64, 15, -59, 40, 82, -17, 16, 24]
#
# result = [number for number in numlist if number > 0 and number %3 ==0 and number %4 !=0]
#
# print(result)

# Напишите функцию которая принимает на вход список.
# Функция создает из этого списка новый список из квадратных корней
# чисел (если число положительное) и самих чисел (если число отрицательное)
# и возвращает результат (желательно применить генератор и тернарный
# оператор при необходимости). В результате работы функции исходный список
# не должен измениться.

import math

old_list = [1, -3, 4, 25, 8, -35, 122, 144]


# первый способ
# def new_sqrt_list (input_list):
#     input_list = input_list.copy()
#     for i in range (len(input_list)):
#         number = input_list[i]
#         if number > 0:
#             input_list[i] = math.sqrt(number)
#     return  input_list
#
# result = new_sqrt_list(old_list)
# print(result)
# print(old_list)

# def new_sqrt_list (input_list):
#     result = [math.sqrt(number) if number >0 else number for number in  input_list ]
#     return result
#
#
# result = new_sqrt_list(old_list)
# print(result)
# print(old_list)

#  Написать функцию которая принимает на вход число от 1 до 100.
#  Если число равно 13, функция поднимает исключительную ситуации
#  ValueError иначе возвращает введенное число, возведенное в квадрат.
# Далее написать основной код программы. Пользователь вводит число.
# Введенное число передаем параметром в написанную функцию и печатаем результат,
# который вернула функция. Обработать возможность
# возникновения исключительной ситуации, которая поднимается внутри функции.

def unlocky_number(number):
    if number == 13:
        raise ValueError('Несчастливое число')
    else:
        return number ** 2


number = int(input('Введите число'))

try:
    result = unlocky_number(number)
except ValueError:
    print('У нас не счастивое число')
else:
    print(result)
