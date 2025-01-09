import random
a = random.randint(1,100)
for i in range (5):
    answer = int(input("Какое это число"))
    if answer !=a :
        if answer > a:
            print("Неизвестное число меньше")
        else:
            print("Неизвестное число больше")
    else:
        print("Вы отгадали")
        break
    if i == 4:
        print("Вы проиграли")
    else:
        continue