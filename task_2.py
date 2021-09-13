n = int(input("Введите n: "))
num = (i for i in range(1, n + 1, 2))
for j in num:
    print(j)