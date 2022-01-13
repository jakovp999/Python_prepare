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
# def my_filter(numbers, function):
#     result = []
#     for number in numbers:
#         if function (number):
#             result.append(number)
#     return result
#
# numbers = [1,45,26,78,8,9,12]
#
# #для четных чисел
# def is_even(number):
#     return number % 2 == 0
#
# print(my_filter(numbers, is_even))
# print(my_filter(numbers, lambda number: number % 2 == 0))


#Встроенные функции

# numbers = [1,5,9,7,2,6,45,12,49]
# #Сортировка по возрастанию
# print(sorted(numbers))
# #по убыванию
# print(sorted(numbers, reverse=True))
# print(type (numbers))
#
# names = ['Max', 'Alex', 'Kate']
# print(sorted(names))
#
# #города и численность
# cities =[('Москва',1000),('lasvegas',500), ('Antverpen',2000)]
#
# print(sorted(cities))
# def by_count(city):
#     return city[1]
#
# #сортировка по численности
# print(sorted(cities, key=by_count))
# print(sorted(cities,key=lambda  city: city[1]))

#Фильтр
# numbers = (1,45,26,78,8,9,12)
#
# #для четных чисел
# def is_even(number):
#     return number % 2 == 0
#
# result = filter(is_even, numbers)
# print(result)
# result=list(result)
# print(result)
#
# names = ['Max','Leo', 'Kate']
# print(list(filter(lambda x: len(x) > 3, names)))

#MAP

# numbers = [1,45,26,78,8,9,12]
# print(list(map(lambda  x: x**2,numbers)))
#
# print(list(map(lambda  x: str(x), numbers)))
