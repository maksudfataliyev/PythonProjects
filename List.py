import random
while True:
    try:
        amount = int(input("Введите количество элементов в списке"))
        list1 = []
        for i in range(amount):
            num_value = random.randint(-1000,1000)
            list1.insert(i+1, num_value)
        print(list1)
        while True:
            print("Меню:\n"
                  "1.Минимальный элемент\n"
                  "2.Максимальный элемент\n"
                  "3.Сумма элементов\n"
                  "4.Среднее арифметическое\n"
                  "5.Завершить программу\n")
            choice = int(input("Что сделать"))
            if choice == 1:
                if amount == 0:
                    print("0")
                else:
                    min_number = list1[0]
                    for i in range(amount-1):
                        if min_number>list1[i+1]:
                            min_number = list1[i+1]
                        else:
                            min_number=min_number
                print("Минимальное число:", min_number)
                print(list1)
            elif choice == 2:
                if amount == 0:
                    print("0")
                else:
                    max_number = list1[0]
                    for i in range(amount-1):
                        if max_number > list1[i+1]:
                            max_number=max_number
                        else:
                            max_number = list1[i+1]
                print("Максимальное число", max_number)
                print(list1)
            elif choice == 3:
                if amount == 0:
                    print("0")
                else:
                    total_sum = sum(list1)
                    print(f"Сумма всех чисел{total_sum}")
                print(list1)
            elif choice == 4:
                if amount == 0:
                    print("0")
                else:
                    sr_arifm = sum(list1)/amount
                    print(sr_arifm)
                print(list1)
            elif choice == 5:
                break
            else:
                print("Че")
                break
    except ValueError:
        print("Нормально пиши")
        continue