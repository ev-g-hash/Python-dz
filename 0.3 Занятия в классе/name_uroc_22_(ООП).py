"""
------------------------------------------------------------------------------------
                            ООП (наследование, полиморфирзм, инкапсуляция)
------------------------------------------------------------------------------------
"""

"""
1) Вася продвинулся в программировании и решил создать
небольшую соцсеть и назвал её Person. Помогите Васе создать его первый аккаунт id_1.

Создайте класс Person
Создайте атрибут name внутри класса, и присвойте ему значение "Vasya"
Создайте экземпляр класса и назовите его id_1. Не забывайте про скобки у класса.
Выведите на экран значение атрибута name, который принадлежит экземпляру id_1,
используя print()
"""
# print("Задание 1")
# class Person:
#     name = "Vasya"
#
# id_1 = Person()
#
# print(id_1.name)


"""
2) Вася продолжает создавать свою соцсеть Person. 
И в этот раз ему нужно научиться изменять имена пользователей, с помощью классов.

Создайте класс Person.
Создайте в классе Person, атрибут name со значением "Vasya".
Создайте экземпляр id_1 класса Person.
Создайте в экземпляре id_1, атрибут name со значением "Lena".
Измените в классе Person атрибут name на значение "Masha".
Выведите на экран значение атрибута name класса Person, и экземпляра id_1 с помощью print. 
Каждый результат на отдельной строке, сначала у Person, затем у id_1 (см. пример ниже).
"""
# print("\nЗадание 2")
# class Person:
#     name = "Vasya"
# a = Person.name
# id_1 = Person()
# id_1.name = "Lena"
# b = id_1.name
# id_1.name = "Masha"
# c = id_1.name
#
#
# print(Person.name)
# print(b)
# print(c)

"""
3) У Машеньки день рождения, и она планирует отправиться в парк с единорогами. 
В парке идёт акция, приведи 5 друзей и получишь шапку-единорожку. 
Машенька любит разные весёлые шапки, поэтому пригласила 5 друзей. 
Но в последний момент один из её друзей не смог прийти, 
и она решила пригласить вас на свой день рождения. Помогите Машеньке обрести 
шапку-единорожку.

Создайте пустой класс Holiday (используйте pass внутри класса).
Создайте экземпляр friends.
Создайте 5 атрибутов для экземпляра friends, с именами name1, 
name2...name5 со значениями 'Sveta', 'Katya', 'Lena', 'Natasha', 
'Leonardo DiCaprio' соответственно.
Так как 'Leonardo DiCaprio' не смог прийти, Машенька приглашает вас на свой ДР. 
Измените атрибут name5 на своё имя, или можете использовать любое другое имя.
Часть кода уже написана, вам нужно лишь сделать то, что написано в задании.
"""
# print("\nЗадание 3")
# class Holiday:
#     pass
#
# friends = Holiday()
# friends.name1 = 'Sveta'
# friends.name2 = 'Katya'
# friends.name3 = 'Lena'
# friends.name4 = 'Natasha'
# friends.name5 = 'Leonardo DiCaprio'
#
# friends.name5 = 'Evgeny'
#
# print(friends.name1)
# print(friends.name2)
# print(friends.name3)
# print(friends.name4)
# print(friends.name5)

"""
примерчики
"""
# class Person:
#     def __init__(self, name, gender, age, study, work):
#         self.name = name
#         self.gender = gender
#         self.age = age
#         self.study = study
#         self.work = work
#
#
# id_1 = Person("Вася", "муж.", 18, "колледж", "доставка")
# id_2 = Person("Ярослав", "муж.", 18, "универ", "сварщик")
# id_3 = Person("Маша", "жен.", 18, "колледж", "кассир")
#
# print(id_1.__dict__)

# class Person1:
#     def __init__(self, music, film, what, ufo, ID):
#         self.music = music
#         self.film = film
#         self.what = what
#         self.ufo = ufo
#         self.ID = ID
#
# id_1_1 = Person1("Техно", "Кино", "всё", "объект", 1234)
# print(id_1_1.__dict__)



"""
функции для работы с атрибутами

setattr - создание атрибута или изменение его
getattr - получение значения атрибута
hasattr - проверка наличия атрибута
dejattr - удаление атрибута
"""

"""
setattr
"""

# class Person:
#     pass
#
# id_1 = Person()
# setattr(id_1, "name", "Кирилл")
# print(id_1.__dict__)
# setattr(id_1, "name", "Женя")
# print(id_1.__dict__)
# id_1.name = "Артём"
# print(id_1.__dict__)

# file = {"name": "Alex", "age": 18, "hobby": "film"}
#
# class Person:
#     pass
#
# id_1 = Person()
#
# for k, v in file.items():
#     setattr(id_1, k, v)
#
# print(id_1.__dict__)
# print(id_1.name)

#__________________________________________________
# class Person:
#     pass
#
# id_1 = Person()
# setattr(id_1, "name", "Вася")
# print(id_1.__dict__)
# setattr(id_1, "name", "Маша")
#__________________________________________________

# class Person:
#     setup = ['set_name', 'set_age', 'set_work', 'set_study']
#
# id_1 = Person()
#
# for i in id_1.setup:
#     setattr(id_1, i, input())
#
# print(id_1.__dict__)
#
# for i in id_1.setup:
#     print(getattr(id_1, i))

"""
getattr
"""
# class Person:
#     name = "Вася"
#     age = 14
#
# person_1 = Person()
#
# print(getattr(person_1, "name", False))
# print(getattr(person_1, "age", False))

# file = ["name", "age", "hobby", "lolo"]
#
# class Person:
#     hobby = "films"
#
# for v in file:
#     if getattr(Person, v, False):
#         print(v)

















