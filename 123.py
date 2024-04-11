"""16.Формируется матрица F следующим образом: если в Е минимальный элемент в нечетных столбцах в области 1 больше,
чем сумма чисел в нечетных строках в области 3, то поменять в В симметрично области 3 и 2 местами, 
иначе В и Е поменять местами несимметрично. При этом матрица А не меняется. 
После чего вычисляется выражение: (К*F)*А– K*AT . Выводятся по мере формирования А, F и все матричные операции последовательно.
 Вид матрицы A:
 E B
 D C

 Каждая из матриц B,C,D,E имеет вид:    1
                                      4   2
                                        3 
"""
import random

# Вводим K и N с клавиатуры
K = int(input("Введите значение K: "))
N = int(input("Введите значение N: "))

' Создаем матрицы B, C, D, E и заполняем их случайными числами'
B = [[random.randint(-10, 10) for j in range(N//2)] for i in range(N//2)]
C = [[random.randint(-10, 10) for j in range(N//2)] for i in range(N//2)]
D = [[random.randint(-10, 10) for j in range(N//2)] for i in range(N//2)]
E = [[random.randint(-10, 10) for j in range(N//2)] for i in range(N//2)]

'Создаем матрицу А'
A = [[0] * N for _ in range(N)]
for i in range(N // 2):
    for j in range(N // 2):
        A[i][j] = E[i][j]
for i in range(N // 2, N):
    for j in range(N // 2):
        A[i][j] = D[i - N // 2 -1][j]
for i in range(N // 2):
    for j in range(N // 2, N):
        A[i][j] = B[i][j - N // 2-1]
for i in range(N // 2, N):
    for j in range(N // 2, N):
        A[i][j] = C[i -N // 2-1][j - N // 2-1]

print("Матрица A")
for i in range(len(A)):
    for j in range(len(A)):
        print("{:4d}".format(A[i][j]), end=' ')
    print()
print()

min_element = 0
'2 область в E'
for i in range((N // 2)):
    for j in range(i, (N // 2) - i):
        if i < len(E) and j < len(E[i]):
            if j % 2 != 0:
                min_element = min(min_element, E[i][j])
print("Минимальный элемент:", min_element)

total_sum = 0
'4 область в E'
for i in range((N // 2) // 2, N // 2):
    for j in range((N // 2) - i - 1, i + 1):
        if i < len(E) and j < len(E[i]):
            if i % 2 != 0:
                total_sum += E[i][j]
print("Сумма элементов:", total_sum)

F = [[0] * N for _ in range(N)]
if min_element > total_sum:
    for i in range(N // 2):
        for j in range(N // 2):
            F[i][j] = E[i][j]
    for i in range(N // 2, N):
        for j in range(N // 2):
            F[i][j] = D[i - N // 2][j]
    for i in range(N // 2, N):
        for j in range(N // 2, N):
            F[i][j] = B[i - N // 2][j - N // 2]
    for i in range(N // 2):
        for j in range(N // 2, N):
            F[i][j] = C[i][j - N // 2]
else:
    for i in range(N // 2):
        for j in range(N // 2):
            F[i][j] = E[i][j]
    for i in range(N // 2, N):
        for j in range(N // 2):
            F[i][j] = D[i - N // 2][j]
    for i in range(N // 2):
        for j in range(N // 2, N):
            F[i][j] = B[i][j - N // 2]
    for i in range(N // 2, N):
        for j in range(N // 2, N):
            F[i][j] = C[i - N // 2][j - N // 2]

print("Матрица F, созданная по условию")
for i in range(len(F)):
    for j in range(len(F)):
        print("{:4d}".format(F[i][j]), end=' ')
    print()
print()


answer = [[0] * N for _ in range(N)]
for i in range(N):
    for j in range(N):
        for k in range(N):
            answer[i][j] += (k * F[i][k]) * A[k][j]

print("Матрица (K*F)*A")
for i in range(len(answer)):
    for j in range(len(answer)):
        print("{:4d}".format(answer[i][j]), end=' ')
    print()
print()


change = [[False] * (N) for _ in range(N)]
for i in range(len(A)):
    for j in range(len(A)):
        if change[i][j] == False:
            A[i][j], A[j][i] = A[j][i], A[i][j]
            change[i][j] = change[j][i] = True


print("Матрица A^T")
for i in range(len(A)):
    for j in range(len(A)):
        print("{:4d}".format(A[i][j]), end=' ')
    print()
print()

answer1 = [[0] * N for _ in range(N)]
for i in range(N):
    for j in range(N):
        for k in range(N):
            answer1[i][j] += answer[i][k] - (k * A[k][j])
print("Матрица (К*F)*А– K*A^T")
for i in range(len(answer1)):
    for j in range(len(answer1)):
        print("{:4d}".format(answer1[i][j]), end=' ')
    print()
print()
