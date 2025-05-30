"""
Задача 1: Подсчет частоты слов
Напишите функцию, которая принимает строку и возвращает словарь,
где ключами являются слова, а значениями — количество их вхождений в строку.
"""
def my_str(line):

    my_dict_str_1 = {i: line.count(i) for i in line}

    return my_dict_str_1

str_input = "привет питон люблю питон питон класс".split()

print("\nЗадача 1 функция: ключи(слова), значения(количество вхождений): ")
print(my_str(str_input))

"""
Задача 2: Слияние двух словарей
Напишите функцию, которая принимает два словаря и возвращает новый словарь, 
который содержит все ключи из обоих словарей. Если ключи совпадают, значения 
должны суммироваться.
"""
def my_dict_summ(dict_1, dict_2):

    summ_dict = dict_1.copy()

    for key, value in dict_2.items():
        if key in summ_dict:
            summ_dict[key] += value
        else:
            summ_dict[key] = value

    return summ_dict

dict_input_1 = {'привет': 1, 'питон': 3, 'люблю': 1, 'класс': 1}
dict_input_2 = {'до свидание': 1, 'питон': 3, 'люблю': 1, 'класс': 4}

print("\nЗадача 2 функция: принимает два словаря, значения при совпадении суммируются: ")
print(my_dict_summ(dict_input_1, dict_input_2))

"""
Задача 3: Находите максимальное значение
Напишите функцию, которая принимает словарь и возвращает ключ с максимальным значением.
"""
def my_dict_max(input_dict):

    max_key = max(input_dict, key=input_dict.get)

    return max_key

dict_input_3 = {'привет': 1, 'питон': 3, 'люблю': 1, 'класс': 2}

print("\nЗадача 3 функция: возвращает ключ с максимальным значением: ")
print(my_dict_max(dict_input_3))

"""
Задача 4: Инвертировать словарь
Напишите функцию, которая принимает словарь и возвращает новый словарь,
где ключи и значения поменяны местами.
"""
def my_dict_revers(input_dict):

    my_dict_r = {x: i for i, x in input_dict.items()}

    return my_dict_r

dict_input_4 = {'привет': 1, 'питон': 2, 'люблю': 3, 'класс': 4}

print("\nЗадача 4 функция: меняет ключ и значение местами: ")
print(my_dict_revers(dict_input_4))

"""
Задача 5: Сортировка словаря по значениям
Напишите функцию, которая принимает словарь и возвращает новый словарь, 
отсортированный по значениям.
"""
#------------------------------------------------------сортировка по возрастанию
def my_dict_sort_v(input_dict):

    sorted_dict = dict(sorted(input_dict.items(), key=lambda elem: elem[1]))

    return sorted_dict

dict_input_5 = {'привет': 5, 'питон': 7, 'люблю': 3, 'класс': 6}

print("\nЗадача 5 функция: сортировка по значению по возрастанию: ")
print(my_dict_sort_v(dict_input_5))
#------------------------------------------------------сортировка по убыванию
def my_dict_sort_y(input_dict):

    sorted_dict_r = dict(sorted(input_dict.items(), key=lambda elem: elem[1])[::-1])

    return sorted_dict_r

dict_input_5_1 = {'привет': 5, 'питон': 7, 'люблю': 3, 'класс': 6}

print("\nЗадача 5 функция: сортировка по значению по убыванию: ")
print(my_dict_sort_y(dict_input_5_1))

"""
Задача 6: Удаление элементов по значению
Напишите функцию, которая принимает словарь и значение, и удаляет все элементы 
из словаря с данным значением.
"""
def my_dict_del(input_dict, elem):

    val_del = [i for i, value in input_dict.items() if value == elem]

    for i in val_del:
        del input_dict[i]

    return input_dict

dict_input_6 = {'привет': 5, 'питон': 7, 'люблю': 3, 'класс': 6}

print("\nЗадача 6 функция: удаляет элемент по заданному значению: ")
print(my_dict_del(dict_input_6, 5))

"""
Задача 7: Группировка элементов
Напишите функцию, которая принимает список строк и возвращает словарь,
где ключами являются первые буквы строк, а значениями — списки строк,
начинающихся на эти буквы.
"""
print("\nЗадача 7 функция: создаёт словарь из первых букв: ")

def my_dict_str(my_sps):

    my_result = {}

    for i in str_input:
        j = i
        my_dict = {i: j for i in j if i == j[0]}
        my_result.update(my_dict)

    return my_result

str_input = "питон люблю класс страна наша академия".split()

print(my_dict_str(str_input))

"""
Задача 8: Проверка на анограммы
Напишите функцию, которая принимает два слова и возвращает True, 
если они являются анограммами (содержат одни и те же буквы в разном порядке), 
и False в противном случае.
"""
print("\nЗадача 8 функция: проверяет слово на анограмму: ")
def my_ano(input_list1, input_list2):

    my_dict_str_1 = {i: input_list1.count(i) for i in input_list1}
    my_dict_str_2 = {i: input_list2.count(i) for i in input_list2}

    return my_dict_str_1 == my_dict_str_2

str_input_1 = "привет"
str_input_2 = "пртвеи"

print(my_ano(str_input_1, str_input_2))
#--------------------------------------------------------для строки
print("\nЗадача 8 функция: проверяет строку на анограмму: ")
def my_ano_str(input_list3, input_list4):

    my_dict_str_3 = {i: input_list3.count(i) for i in input_list3}
    my_dict_str_4 = {i: input_list4.count(i) for i in input_list4}

    return my_dict_str_3 == my_dict_str_4

str_input_3 = "привет привет да нет питон да".split()
str_input_4 = "нет привет питон да да привет".split()

print(my_ano_str(str_input_3, str_input_4))