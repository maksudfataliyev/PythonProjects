def a():
    print("Don't compare yourself with anyone in this world\n"
            "if you do so, you are insulting yourself.\n"
            "Bill Gates")
    a()
while True:
    try:
        def b(x,y):
            list1 = []
            for i in range(y-(x+1)):
                num = (x + (i + 1))
                if num%2 == 0:
                    list1.append(num)
                else:
                    continue
            print(list1)
            return list1
        x = int(input("x"))
        y = int(input("y"))
        b(x,y)
        break
    except ValueError:
        print("заново")
        continue
while True:
    try:
        def c(x,y,z):
            if z == True:
                for i in range(x):
                    print(x*y)
            else:
                print(x*y)
                for i in range(x-2):
                    print(y+(x-2)*" "+y)
                print(x*y)
        q = int(input("Высота"))
        w = input("Какой символ")
        e = bool(int(input("0(пусто)1(заполнить)")))
        c(q,w,e)
        break
    except ValueError:
        print("Заново")
        continue
while True:
    try:
        def d(q,w,e,r,t):
            list1 = [q,w,e,r,t]
            min_number = min(list1)
            print("Минимальное число",min_number)
            return min_number
        num1 = int(input())
        num2 = int(input())
        num3 = int(input())
        num4 = int(input())
        num5 = int(input())
        d(num1,num2,num3,num4,num5)
        break
    except ValueError:
        print("Заново")
        continue
while True:
    try:
        def e(a,b):
            if a>b:
                number = 1
                for i in range(a-(b+1)):
                    c = b + i + 1
                    number = number * c
                print("Произведенние", number)
            else:
                number = 1
                for i in range(b-(a+1)):
                    c = a + i + 1
                    number = number * c
                print("Произведение", number)
            return number
        v = int(input("Верхняя граница"))
        q = int(input("Нижняя граница"))
        e(q,v)
        break
    except ValueError:
        print("Заново")
        continue
while True:
    try:
        def f(a):
            b = abs(a)
            print(len(str(b)))
            return b
        m = int(input("Введите число"))
        f(m)
        break
    except ValueError:
        print("Заново")
        continue
while True:
    try:
        def g(lk):
            l = str(lk)
            if l == l[::-1]:
                print(bool(1))
                return True
            else:
                print(bool(0))
                return False
        l = int(input("Введите число"))
        g(l)
        break
    except ValueError:
        print("Занов")
        continue
