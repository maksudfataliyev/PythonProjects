1.
n = int(input("Нечетное число"))
if n % 2 == 0:
    print("нет")
else:
    c = n // 2
    for i in range(n):
        if i <= c:
            s = (2 * i) + 1
        else:
            s = (2 * (n - i - 1)) + 1
        sp = (n - s)//2
        print(" " * sp + "*" * s)


2.
height = int(input("Нечетное число"))

if height % 2 == 0:
    print("Нечетное надо")
else:
    for i in range(height):
        num_spaces = abs(height // 2 - i)
        if i == 0 or i == height - 1:
            inner_part = '*'
        else:
            inner_spaces = abs(2 * (height // 2 - num_spaces) - 1)
            inner_part = '*' + ' ' * inner_spaces + '*'

        print(' ' * num_spaces + inner_part)

3.
height = int(input("Высота"))

for i in range(height):
    if i == 0:
        print('*' * (2 * height - 1))
    elif i < height - 1:
        inner_spaces = ' ' * (2 * (height - i - 1) - 1)
        print(' ' * i + '*' + inner_spaces + '*')
    else:
        print(' ' * i + '*')