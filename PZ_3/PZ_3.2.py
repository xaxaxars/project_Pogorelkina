
# Задача 1: Проверка, что ровно одно число положительное

try:
    A = int(input("Введите число A: "))
    B = int(input("Введите число B: "))
    C = int(input("Введите число C: "))

    positives = 0
    if A > 0:
        positives += 1
    if B > 0:
        positives += 1
    if C > 0:
        positives += 1

    if positives == 1:
        print("Утверждение истинно: ровно одно число положительное.")
    else:
        print("Утверждение ложно.")
except ValueError:
    print("Ошибка: вводите только целые числа.")
