import random

# Генерация матрицы A и ее подматриц (B, C, D, E)
def generate_matrix(N):
    A = [[0] * N for _ in range(N)]

    # Генерация значений для подматриц B, C, D, E
    for i in range(N):
        for j in range(N):
            # Подматрица B
            if i >= N // 2 and j < N // 2:
                A[i][j] = random.randint(-10, 10)
            # Подматрица C
            elif i >= N // 2 and j >= N // 2:
                A[i][j] = random.randint(-10, 10)
            # Подматрица D
            elif i < N // 2 and j >= N // 2:
                A[i][j] = random.randint(-10, 10)
            # Подматрица E
            else:
                A[i][j] = random.randint(-10, 10)

    return A

# Формирование матрицы F
def form_matrix_F(B, E):
    min_in_odd_cols = min(E[i][j] > 0 for i in range(len(E) // 2) for j in range(len(E) // 2, len(E)))
    sum_in_odd_rows = sum(B[i][j] < 0 for i in range(len(B) // 2, len(B)) for j in range(len(B) // 2, len(B)))

    if min_in_odd_cols > sum_in_odd_rows:
        # Поменять в B симметрично области 3 и 2
        n = len(B)
        for i in range(n // 4, n // 2):
            B[i], B[n - i - 1] = B[n - i - 1], B[i]
    else:
        # Поменять B и E местами несимметрично
        B, E = E, B

    return B

# Вычисление выражения (KF)*A - K * A^T
def calculate_F(K, F, A, AT):
    result_matrix = [[(K * F[i][j]) * A[i][j] - K * AT[j][i] for j in range(len(F))] for i in range(len(F))]
    return result_matrix

def main():
    K = int(input("Введите число K: "))
    N = int(input("Введите размер матрицы N (четное и больше 6): "))

    # Генерация матрицы A(N,N) и ее подматриц B, C, D, E
    A = generate_matrix(N)
    print("\nМатрица A:")
    for row in A:
        print(row)

    # Создание матриц B, C, D, E
    B = [row[:N//2] for row in A[:N//2]]
    E = [row[N//2:] for row in A[N//2:]]

    # Формирование матрицы F
    F = form_matrix_F(B, E)
    print("\n Матрица F:")
    for row in F:
        print(row)

    # Вычисление выражения (K*F)*A - K * A^T
    AT = [[row[i] for row in A] for i in range(len(A))]
    result_matrix = calculate_F(K, F, A, AT)

    # Вывод результатов
    print("\n Результат выражения (K*F)*A - K * A^T:")
    for row in result_matrix:
        print(row)

main()
