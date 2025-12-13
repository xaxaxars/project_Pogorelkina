#1. Дано вещественное число A и целое число N (>0). Используя один цикл, найти сумму:1 + A + A² + A³ + ... + Aᴺ.
try:
    A = float(input("Введи число A: "))
    N = int(input("Введи целое число N (>0): "))
    if N <= 0:
        print("N должно быть больше нуля.")
    else:
        total = 0
        power = 1  # A^0
        for _ in range(N + 1):
            total += power
            power *= A
        print("Сумма 1 + A + A^2 + ... + A^N равна", total)
except ValueError:
    print("Ошибка: проверьте правильность ввода чисел.")
