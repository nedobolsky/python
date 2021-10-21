num = input('Введите целое положительное число ')
len_num = len(num)
num = int(num)
a = num % 10

while len_num != 0:
    num = num // 10
    b = num % 10
    if a < b:
        b, a = a, b
    len_num -= 1
print(a)
