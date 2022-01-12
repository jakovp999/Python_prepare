# def my_filter(numbers):
#     result = []
#     for number in numbers:
#         if number % 2 ==0:
#             result.append(number)
#     return result
#
#
# numbers = [1,45,26,78,8,9,12]
# print(my_filter(numbers))

#параметр в виде функции
# def my_filter(numbers, function):
#     result = []
#     for number in numbers:
#         if function (number):
#             result.append(number)
#     return result

# numbers = [1,45,26,78,8,9,12]
#
# #для четных чисел
# def is_even(number):
#     return number % 2 == 0
#
# print(my_filter(numbers, is_even))
#
# # для нечетных чисел
# def is_not_even(number):
#     return number % 2 != 0
#
# print(my_filter(numbers, is_not_even))
#
# #число больше 4
#
# def big_4(number):
#     return (number) > 4
# print(my_filter(numbers, big_4  ))

# print(my_filter(numbers))


#Лямбда функции
def my_filter(numbers, function):
    result = []
    for number in numbers:
        if function (number):
            result.append(number)
    return result

numbers = [1,45,26,78,8,9,12]

#для четных чисел
def is_even(number):
    return number % 2 == 0

print(my_filter(numbers, is_even))
print(my_filter(numbers, lambda number: number % 2 == 0))