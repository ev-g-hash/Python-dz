# -------------------------------------------------------Задание 1
# Пользователь вводит с клавиатуры номер дня недели
# (1-7). Необходимо вывести на экран названия дня неде-
# ли. Например, если 1, то на экране надпись понедельник,
# вторник и т.д.
#-----------------------------------------------------------------
print("""\nПрограмма "дни недели"
для завершения программы напишите ( завершить ) \n""")
while True:
    day_week = input("введите день недели ( 1-7 ): ").lower()
    if day_week.isdigit():
        day_week = int(day_week)
        if day_week == 1:
            print("понедельник")
        elif day_week == 2:
            print("вторник")
        elif day_week == 3:
            print("среда")
        elif day_week == 4:
            print("четверг")
        elif day_week == 5:
            print("пятница")
        elif day_week == 6:
            print("суббота")
        elif day_week == 7:
            print("воскресенье")
        else:
            print("ошибка, введите цифру в диапазоне от 1 до 7")
    elif day_week == "завершить":
        print("программа завершила работу")
        break
    else:
        print("ошибка, вы ввели буквы, введите цифры")

# -------------------------------------------------------Задание 2
# Пользователь вводит с клавиатуры номер месяца
# (1-12). Необходимо вывести на экран название месяца.
# Например, если 1, то на экране надпись январь, 2—фев-
# раль и т.д.
#-----------------------------------------------------------------
print("""\nпрограмма "месяцы" """)
month = int(input("введите номер месяца ( от 1 до 12 ): "))

if month == 1:
    print("январь")
elif month == 2:
    print("февраль")
elif month == 3:
    print("март")
elif month == 4:
    print("апрель")
elif month == 5:
    print("май")
elif month == 6:
    print("июнь")
elif month == 7:
    print("июль")
elif month == 8:
    print("август")
elif month == 9:
    print("сентябрь")
elif month == 10:
    print("октябрь")
elif month == 11:
    print("ноябрь")
elif month == 12:
    print("декабрь")
else:
    print("ошибка, неверно введён месяц")

# -------------------------------------------------------Задание 3
# Пользователь вводит с клавиатуры число. Если число
# больше нуля нужно вывести надпись «Number is positive»,
# если меньше нуля «Number is negative», если равно нулю
# «Number is equal to zero»
#-----------------------------------------------------------------
print("""\nпрограмма "zero" """)
num = int(input("введите число: "))

if num == 0:
    print("Number is equal to zero")
elif num >= 0:
    print("Number is pozitive")
elif num <= 0:
    print("Number is negative")

# -------------------------------------------------------Задание 4
# Пользователь вводит два числа. Определить, равны
# ли эти числа, и, если нет, вывести их на экран в порядке
# возрастания.
#-----------------------------------------------------------------
print("""\nпрограмма "по порядку" """)
num_1 = int(input("введите первое число: "))
num_2 = int(input("введите второе число: "))

if num_1 > num_2:
    print(f"{num_2}, {num_1}")
elif num_2 > num_1:
    print(f"{num_1}, {num_2}")
else:
    print("числа равны")
