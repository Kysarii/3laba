# 3laba
"""
Задание:
С клавиатуры вводится два числа K и N. Квадратная матрица А(N,N), состоящая из 4-х равных по размерам подматриц B,C,D,E
заполняется случайным образом целыми числами в интервале [-10,10]. Для тестирования использовать не случайное заполнение,
а целенаправленное.

Вариант 16
Формируется матрица F следующим образом: если в Е минимальный элемент в нечетных столбцах в области 1 больше,
чем сумма чисел в нечетных строках в области 3, то поменять в В симметрично области 3 и 2 местами, иначе В и Е поменять 
местами несимметрично. При этом матрица А не меняется. После чего вычисляется выражение: (К*F)*А– K*AT . 
Выводятся по мере формирования А, F и все матричные операции последовательно.
"""
