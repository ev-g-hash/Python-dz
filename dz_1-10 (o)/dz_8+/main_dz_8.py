"""
Задание 1
Пользователь вводит с клавиатуры два числа. Нужно
посчитать отдельно сумму четных, нечетных и чисел,
кратных 9 в указанном диапазоне, а также среднеариф-
метическое каждой группы.
"""
start = int(input("введите первое число (начало диапазона): "))
end = int(input("введите второе число (конец диапазона): "))

x = []
y = []
z = []

for i in range(start, end + 1):
    if i % 2 == 0:
        x.append(i)

    if i % 2:
        y.append(i)

    if not i % 9:
        z.append(i)

print(f"""
- сумма четных чисел диапазона равна: ( {sum(x)} )
- среднеарифметическое чётной группы ( {sum(x) / len(x)} )""")

print(f"""
- сумма нечетных чисел диапазона равна: ( {sum(y)} )
- среднеарифметическое нечётной группы ( {sum(y) / len(y)} )""")

print(f"""
- сумма кратных "9" этого диапазона ( {sum(z)} ),
- среднеарифметическое кратной группы ( {sum(z) / len(z)} )\n""")

print(f"""* чётные числа диапазона: {x}""")
print(f"""* нечётные числа диапазона: {y}""")
print(f"""* кратное 9 этого диапазона: {z}""")

"""
Задание 2
Пользователь вводит с клавиатуры длину линии и символ для заполнения линии. 
Нужно отобразить на экране вертикальную линию из введенного символа, указанной длины.
Например, если было введено 5 и символ %, тогда вывод на экран будет такой:
                                            %
                                            %
                                            %
                                            %
                                            %
"""
print()
length = int(input("введите длину линии в цифрах (например 7): "))
symbol = input("введите символ (например % или g или & и т.д.): ")

for i in range(0, length):
    x = symbol

    print("\t" * 17, x)

"""
Задание 3
Пользователь вводит с клавиатуры числа. Если число больше нуля нужно вывести 
надпись «Number is positive», если меньше нуля «Number is negative», 
если равно нулю «Number is equal to zero». Когда пользователь вводит
число 7 программа прекращает работу и выводит на экран надпись «Good bye!»
"""
while True:
    x = int(input("введите число: "))
    if x > 0 and x != 7:
        print("Number is positive")
    elif x < 0:
        print("Number is negative")
    elif x == 0:
        print("Number is equal to zero")
    elif x == 7:
        print("Good bye!")
        break


"""
Задание 4
Пользователь вводит с клавиатуры числа. Програм-
ма должна подсчитывать сумму, максимум и минимум,
введенных чисел. Когда пользователь вводит число 7
программа прекращает свою работу и выводит на экран
надпись «Good bye!»
"""
i = []
while True:
    x = int(input("число: "))
    i.append(x)
    if x == 7:
        print("Good bye!")
        break

    print(f"введенные числа {i}")
    print(f"сумма {sum(i)}")
    print(f"max {max(i)}")
    print(f"min {min(i)}")















