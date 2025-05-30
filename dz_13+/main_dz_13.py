"""
----------------------------------------------------------------------------------------------
Задание 1
В списке целых, заполненном случайными числами вычислить:
negative         - Сумму отрицательных чисел;
even             - Сумму четных чисел;
odd              - Сумму нечетных чисел;
multi_3          - Произведение элементов с индексами кратными 3;
multi_x, multi_y - Произведение элементов между минимальным и максимальным элементом;
el_1, el_2       - Сумму элементов,находящихся между первыми и последним положительными элементами.
 -----------------------------------------------------------------------------------------------
"""
from random import randint

num = []

for i in range(7):
    num.append(randint(-10, 10))

print(f"случайные числа {num}")

negative = 0
even = 0
odd = 0
multi_3 = 1

#----------------------------------Сумма отрицательных чисел----------------------------------------
for i in num:
    if i < 0:
        negative += i
print(f"сумма отрицательных чисел {negative}")

#-------------------------------------Сумма четных чисел-------------------------------------------
for i in num:
    if i == 0:
        continue
    if i % 2 == 0:
        even += i
print(f"сумма четных чисел {even}")

#------------------------------------Сумма нечетных чисел-------------------------------------------
for i in num:
    if i % 2:
        odd += i
print(f"сумма нечетных чисел {odd}")

#--------------------------Произведение элементов с индексами кратными 3----------------------------
for i in range(len(num)):
    if i == 0:
        continue
    if i % 3 == 0:
        multi_3 *= num[i]
print(f"произведение элементов с индексами кратными 3 = {multi_3}")

#-------------------Произведение элементов между минимальным и максимальным элементом---------------
print()
print(f"случайные числа {num}")

y = num.index(min(num))
x = num.index(max(num))

multi_x = 1
multi_y = 1
z = []

if x < y:
    for i in num[x + 1:y]:
        z.append(i)
        multi_x *= i
    print(f"числа в диапазоне между {[max(num)]} и {[min(num)]} = {z}")

    if multi_x == 1:
        print("между минимальным и максимальным элементом нет чисел")
    else:
        print(f"произведение этих чисел = {multi_x}")

if y < x:
    for i in num[y + 1:x]:
        z.append(i)
        multi_y *= i
    print(f"числа в диапазоне между {[min(num)]} и {[max(num)]} = {z}")

    if multi_y == 1:
        print("между минимальным и максимальным элементом нет чисел")
    else:
        print(f"произведение этих чисел = {multi_y}")

#----------Сумма элементов,находящихся между первыми и последним положительными элементами----------
print()
ind = [] #индексы

for index, i in enumerate(num):
    if i > 0:
        ind.append(index)

el_1 = ind[0]
el_2 = ind[-1]
el = 0

for i in num[el_1 + 1:el_2]:
    el += i

print(f"первое положительное число ( {num[el_1]} ), второе последнее положительное число ( {num[el_2]} )")
print(f"сумма чисел между ними = {el}")

"""
---------------------------------------------------------------------------------------------------
 Задание 2
 Есть список целых,заполненный случайными числами. На основании данных этого массива нужно:
 ■ Создать список целых, содержащий только четные числа из первого списка;
 ■ Создать список целых,содержащий только нечетные числа из первого списка;
 ■ Создать список целых, содержащий только отрицательные числа из первого списка;
 ■ Создать список целых, содержащий только положительные числа из первого списка
 -------------------------------------------------------------------------------------------------
"""
print()
from random import randint

numbers = []

for i in range(10):
    numbers.append(randint(-20, 20))
print(f"список случайных чисел {numbers}")

#------------------Cписок целых, содержащий только четные числа из первого списка-----------------
even_num = []

for i in numbers:
    if not i % 2:
        even_num.append(i)
print(f"список чётных чисел {even_num}")

#------------------Список целых,содержащий только нечетные числа из первого списка-----------------

odd_num = []

for i in numbers:
    if i % 2:
        odd_num.append(i)
print(f"список нечётных чисел {odd_num}")

#------------------Список целых,содержащий только отрицательные числа из первого списка-----------------

negative_num = []

for i in numbers:
    if i < 0:
        negative_num.append(i)
print(f"список отрицательных чисел {negative_num}")

#------------------Список целых,содержащий только положительные числа из первого списка-----------------

positive_num = []

for i in numbers:
    if i > 0:
        positive_num.append(i)
print(f"список положительных чисел {positive_num}")