#Задание 1


def multiply(list1):
    mult = 1
    for i in range(len(list1)):
        try:
            if str(list1[i]).endswith(".0"):
                list1[i] = int(list1[i])
            else:
                pass
        except ValueError:
            pass
        if type(list1[i]) is int:
            mult = mult * list1[i]
        else:
            continue
    print(f"произведение всех целых чисел {mult}")
    return mult
list1 = []
while True:
    try:
        number = float(input("Напиши любое число"))
        list1.append(number)
        print(list1)
    except ValueError:
        print("Нормально пиши")
        continue
    try:
        number1 = int(input("Напиши целое число"))
        list1.append(number1)
        print(list1)
    except ValueError:
        print("Нормально пиши")
        continue
    try:
        choice = int(input("Продолжить(1) или закончить добавлять элементы в список(любое число)"))
        if choice == 1:
            continue
        else:
            break
    except ValueError:
        print("Нормально пиши")
print(list1)
multiply(list1)

#Задание 2
def minimum(list1):
    min_number = list1[0]
    for i in range(len(list1) - 1):
        if min_number > list1[i+1]:
            min_number = list1[i+1]
        else:
            min_number = min_number
    print(f"минимальное число {min_number}")
    return min_number
minimum(list1)



#Задание 4

def remove_number(list1,del_num):
    count = 0
    while del_num in list1:
        list1.remove(del_num)
        count = count + 1
    print(list1)
    print(f"количество удалённых чисел:{count}")
    return count
while True:
    try:
        delnum = int(input("Какое целое число удалить"))
        break
    except:
        print("Нормально пиши")
        continue

remove_number(list1,delnum)

#Задание 5

def lists_together(list1,list2):
    list1.extend(list2)
    print(f"новый лист:{list1} так как к нему я прибавил {list2}")
    return list1

list2 = [2,3,5]

lists_together(list1,list2)

#Задание 3
def dinar(list1):
    list7 = []
    for c in list1:
        if c <= 1:
            continue
        for i in range(2, c):
            if c % i == 0:
                break
        else:
            list7.append(c)
    print(f"Простые числа: {list7}")
    return list7
dinar(list1)

#Задание 6
def stepen(list5,stepen_num):
    list1 = []
    for i in list5:
        list1.append(i**stepen_num)
    print(f"список с новыми числами в степени {list1}")
    return list1
while True:
    try:
        st = int(input("В какой степени будут числа"))
        break
    except ValueError:
        print("Нормально пиши")
        continue
stepen(list1,st)

