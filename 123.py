#16.Формируется матрица F следующим образом: если в Е минимальный элемент в нечетных столбцах в области 1 больше,
#чем сумма чисел в нечетных строках в области 3, то поменять в В симметрично области 3 и 2 местами, 
#иначе В и Е поменять местами несимметрично. При этом матрица А не меняется. 
#После чего вычисляется выражение: (К*F)*А– K*AT . Выводятся по мере формирования А, F и все матричные операции последовательно.
import random

# Генерация матрицы A и ее подматриц (B, C, D, E)
def generate_matrix(N):
    A = [[0] * N for _ in range(N)]

    # Генерация значений для подматриц B, C, D, E
    for i in range(N):
        for j in range(N):
            if i >= N // 2 and j < N // 2:
                A[i][j] = random.randint(-10, 10)
            elif i >= N // 2 and j >= N // 2:
                A[i][j] = random.randint(-10, 10)
            elif i < N // 2 and j >= N // 2:
                A[i][j] = random.randint(-10, 10)
            else:
                A[i][j] = random.randint(-10, 10)

    return A

# Формирование матрицы F
def form_matrix_F(B, E):
    min_in_odd_cols = min(E[i][j] > 0 for i in range(len(E) // 2) for j in range(len(E) // 2, len(E)))
    sum_in_odd_rows = sum(B[i][j] < 0 for i in range(len(B) // 2, len(B)) for j in range(len(B) // 2, len(B)))

    if min_in_odd_cols > sum_in_odd_rows:
        n = len(B)
        for i in range(n // 4, n // 2):
            B[i], B[n - i - 1] = B[n - i - 1], B[i]
    else:
        B, E = E, B

    return B

# Вычисление выражения
def calculate_F(K, F, A, AT):
    result_matrix = [[(K * F[i][j]) * A[i][j] - K * AT[j][i] for j in range(len(F))] for i in range(len(F))]
    return result_matrix

def main():
    K = int(input("Введите число K: "))
    N = int(input("Введите размер матрицы N (четное и больше 6): "))

    A = generate_matrix(N)
    print("\nМатрица A:")
    for row in A:
        print(row)

    B = [row[:N//2] for row in A[:N//2]]
    E = [row[N//2:] for row in A[N//2:]]

    F = form_matrix_F(B, E)
    print("\n Матрица F:")
    for row in F:
        print(row)
    AT = [[row[i] for row in A] for i in range(len(A))]
    result_matrix = calculate_F(K, F, A, AT)

    print("\n Результат выражения (K*F)*A - K * A^T:")
    for row in result_matrix:
        print(row)

main()
