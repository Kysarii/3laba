"""16.Формируется матрица F следующим образом: если в Е минимальный элемент в нечетных столбцах в области 1 больше,
чем сумма чисел в нечетных строках в области 3, то поменять в В симметрично области 3 и 2 местами, 
иначе В и Е поменять местами несимметрично. При этом матрица А не меняется. 
После чего вычисляется выражение: (К*F)*А– K*AT . Выводятся по мере формирования А, F и все матричные операции последовательно.
 Вид матрицы A:
 E B
 D C

 Каждая из матриц B,C,D,E имеет вид:    1
                                      4   2
                                        3 """
import random

k = int(input("Введите k: "))
n = int(input("Введите n (четное и больше или равно 6): "))
b = [[random.randint(-10, 10) for i in range(n//2)] for j in range(n//2)]
c = [[random.randint(-10, 10) for i in range(n//2)] for j in range(n//2)]
d = [[random.randint(-10, 10) for i in range(n//2)] for j in range(n//2)]
e = [[random.randint(-10, 10) for i in range(n//2)] for j in range(n//2)]

a = [[0] * n for _ in range(n)]
for i in range(n // 2):
    for j in range(n // 2):
        a[i][j] = e[i][j]
for i in range(n // 2, n):
    for j in range(n // 2):
        a[i][j] = d[i - n // 2 -1][j]
for i in range(n // 2):
    for j in range(n // 2, n):
        a[i][j] = b[i][j - n // 2-1]
for i in range(n // 2, n):
    for j in range(n // 2, n):
        a[i][j] = c[i -n // 2-1][j - n // 2-1]

print("Матрица A")
for i in range(len(a)):
    for j in range(len(a)):
        print("{:4d}".format(a[i][j]), end=' ')
    print()
print()


min_element = float('inf')
for i in range(n // 2+1):
    for j in range(i, n - i):
        if i < len(e) and j < len(e[i]):
            if j % 2 != 0:
                min_element = min(min_element, e[i][j])
print("Минимальный элемент:", min_element)

total_sum = 0
for i in range(n // 2, n):
    for j in range(n - i - 1, i + 1):
        if i < len(e) and j < len(e[i]):
            if i % 2 != 0:
                total_sum += e[i][j]
print("Сумма элементов:", total_sum)

f = [[0] * n for _ in range(n)]
if min_element > total_sum:
    for i in range(n // 2):
        for j in range(n // 2):
            f[i][j] = e[i][j]
    for i in range(n // 2, n):
        for j in range(n // 2):
            f[i][j] = d[i - n // 2][j]
    for i in range(n // 2, n):
        for j in range(n // 2, n):
            f[i][j] = b[i - n // 2][j - n // 2]
    for i in range(n // 2):
        for j in range(n // 2, n):
            f[i][j] = c[i][j - n // 2]
else:
    for i in range(n // 2):
        for j in range(n // 2):
            f[i][j] = e[i][j]
    for i in range(n // 2, n):
        for j in range(n // 2):
            f[i][j] = d[i - n // 2][j]
    for i in range(n // 2):
        for j in range(n // 2, n):
            f[i][j] = b[i][j - n // 2]
    for i in range(n // 2, n):
        for j in range(n // 2, n):
            f[i][j] = c[i - n // 2][j - n // 2]

print("Матрица F, созданная по условию")
for i in range(len(f)):
    for j in range(len(f)):
        print(f[i][j], end=' ')
    print()
print()


answer = [[0] * n for _ in range(n)]
for i in range(n):
    for j in range(n):
        for k in range(n):
            answer[i][j] += (k * f[i][k]) * a[k][j]

print("Матрица (K*F)*A")
for i in range(len(answer)):
    for j in range(len(answer)):
        print(answer[i][j], end=' ')
    print()
print()


change = [[False] * (n) for _ in range(n)]
for i in range(len(a)):
    for j in range(len(a)):
        if change[i][j] == False:
            a[i][j], a[j][i] = a[j][i], a[i][j]
            change[i][j] = change[j][i] = True


print("Матрица A^T")
for i in range(len(a)):
    for j in range(len(a)):
        print(a[i][j], end=' ')
    print()
print()

answer1 = [[0] * n for _ in range(n)]
for i in range(n):
    for j in range(n):
        for k in range(n):
            answer1[i][j] += answer[i][k] - (k * a[k][j])
print("Матрица (К*F)*А– K*A^T")
for i in range(len(answer1)):
    for j in range(len(answer1)):
        print(answer1[i][j], end=' ')
    print()
print()
