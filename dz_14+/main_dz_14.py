"""
Задание 1
Напишите функцию, которая отображает на экран форматированный текст, указанный ниже:
“Don't compare yourself with anyone in this world…
 if you do so, you are insulting yourself.”
                                    Bill Gates
"""
def my_txt():
    txt = """
“Don't compare yourself with anyone in this world…
 if you do so, you are insulting yourself.”
                                    Bill Gates"""
    print(txt)

my_txt()

"""
Задание 2
Напишите функцию, которая принимает два числа в качестве параметра и отображает все четные числа
между ними.
"""
print("чётные числа диапазона:")

def my_even(x, y):

    for _ in range(x, y + 1):
        if not _ % 2:
            print(_, end="; ")

my_even(1, 10)

"""
Задание 3
Напишите функцию, которая отображает пустой или заполненный квадрат из некоторого символа. Функция
принимает в качестве параметров: длину стороны квадрата, символ и переменную логического типа:
■ если она равна True, квадрат заполненный;
■ если False, квадрат пустой.
"""
print("\n")

def my_square(l, s, square=True):

    if square:
        for _ in range(l):
            print(s * l)
    else:
        print(s * l)
        for _ in range(l - 2):
            print(s + "   " * (l - 2) + s)
        print(s * l)

my_square(15, " $ ", square=False)

"""
Задание 4
Напишите функцию, которая возвращает минимальное из пяти чисел. Числа передаются в качестве параметров.
"""
def my_min(a,b,c,d,e):
    print(f"\nминимальное из пяти - ( {min(a,b,c,d,e)} )")

my_min(1,10,3,2,7)

"""
Задание 5
Напишите функцию, которая возвращает произведение чисел в указанном диапазоне. Границы диапазона
передаются в качестве параметров. Если границы диапазона перепутаны (например, 5 - верхняя граница, 
25 - нижняя граница), их нужно поменять местами.
"""
def my_multiply(start, end):

    a = 1
    b = 1

    if start < end:
        for i in range(start, end + 1):
            if i == 0:
                i = 1
            a *= i
    if start > end:
        for i in range(end, start + 1):
            if i == 0:
                i = 1
            b *= i

    if a > b:
        print(f"\nпроизведение чисел в диапазоне от {start} до {end} равно {a}")
    else:
        print(f"\nпроизведение чисел в диапазоне от {end} до {start} равно {b}")

my_multiply(5, 0)

"""
Задание 6
Напишите функцию, которая считает количество цифр в числе. Число передаётся в качестве параметра. Из
функции нужно вернуть полученное количество цифр. Например, если передали 3456, количество цифр будет 4.
"""
def my_len(x):

    y = str(x)
    count = 0

    for _ in y:
        count += 1

    print(f"\nколичество цифр в числе ( {y} ) = ( {count} )")

my_len(12345)

# доп решение 2(float)
# def my_len_1(x):
#     y = str(x)
#     count = 0
#
#     for _ in y:
#         if _ == ".":
#             continue
#         count += 1
#
#     print(y)
#     print(f"количество цифр в числе {y} = ({count})")
#
# my_len_1(12345.001)

"""
Задание 7
Напишите функцию, которая проверяет является ли число палиндромом. Число передаётся в качестве пара-
метра. Если число палиндром нужно вернуть из функции true, иначе false.
«Палиндром» — это число, у которого первая часть цифр равна второй перевернутой части цифр. Например,
123321—палиндром (первая часть 123, вторая 321, которая после переворота становится 123), 
546645—палиндром, а 421987 — не палиндром.
"""
print("\nЕсли число палиндром нужно вернуть из функции true, иначе false.")

def my_pld(n):
    print(f"введённое число ( {n} )")

    n = str(n)

    if n == n[::-1]:
        print(bool(1))
    else:
        print(bool(0))

my_pld(1213)

# def my_pld_1(n):
#     n = str(n)
#     if n == n[::-1]:
#         print("палиндром")
#     else:
#         print("не палиндром")
#
# my_pld_1(121)