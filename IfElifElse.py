#Задание 1:

num1 = float(input("Введите первое число:"))
num2 = float(input("Введите второе число:"))
num3 = float(input("Введите третье число:"))
answer = int(input("Умножение(0) или сумма(1)"))
if answer == 0:
    print(num1 * num2 * num3)
elif answer == 1:
    print(num1 + num2 + num3)
else:
    print("Такого нету")

#Задание 2:

num1 = float(input("Введите первое число:"))
num2 = float(input("Введите второе число:"))
num3 = float(input("Введите третье число:"))
answer = int(input("Максимальное(0) минимальное(1) среднее арифметическое(2)"))
if answer == 0:
    if num1 > num2 and num1 > num3:
        print("Первое число самое большое")
    elif num2 > num3 and num2 > num1:
        print("Второе число самое большое")
    elif num1==num2 and num1==num3:
        print("Числа равны")
    else:
        print("Третье число самое большое")
elif answer == 1:
    if num1 < num2 and num1 < num3:
        print("Первое число самое маленькое")
    elif num2 < num3 and num2 < num1:
        print("Второе число самое маленькое")
    elif num1==num2 and num1==num3:
        print("Числа равны")
    else:
        print("Третье число самое маленькое")
elif answer ==2:
    print((num1 + num2 + num3)/3)

#Задание 3:

meters = float(input("Введите количество метров"))
answer = int(input("Мили(0) дюймы(1) или ярды(2)"))
if answer == 1:
    print(meters * 39.3701)
elif answer == 2:
    print(meters * 1.09361)
elif answer == 0:
    print(meters * 0.000621371)


