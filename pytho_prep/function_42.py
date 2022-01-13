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

#Домашнее задание

# def person_info(name,age,city):
#     result = (f'{name}, {age} год(а) проживает в {city}') # !!!!другой синтаксис не такой как на уроке
#     return  result
#
# print(person_info ('Василий', 21, 'Москва'))
# print(type(person_info))

#поиск максимума
# def get_max(a,b,c):
#     result = max(a,b,c)
#     return result
# result = get_max(9,7,10)
#
# print(result)

# #игра со здоровьем и жизнью
#
# player_name = input('Введите имя игрока')
#
# player = {
#     'name': player_name,
#     'health': 100,
#     'damage': 50,
# }
#
# enemy_name = input('Введите имя врага')
#
# enemy = {
#     'name': enemy_name,
#     'health': 50,
#     'damage': 30,
# }
#
# def attack(unit, target):
#     target['health']-=unit['damage']
#
# attack (player, enemy)
# print(enemy)
#
# attack(enemy, player)
# print(player)

#игра со здоровьем и жизнью  и броня

player_name = input('Введите имя игрока')

player = {
    'name': player_name,
    'health': 100,
    'damage': 50,
    'armor': 1.2
}

enemy_name = input('Введите имя врага')

enemy = {
    'name': enemy_name,
    'health': 50,
    'damage': 30,
    'armor': 1.0
}

def get_damage(damage, armor):
    return damage/ armor


def attack(unit, target):
    damage = get_damage(unit['damage'], target['armor'])
    target['health'] -= damage

attack (player, enemy)
print(enemy)

attack(enemy, player)
print(player)