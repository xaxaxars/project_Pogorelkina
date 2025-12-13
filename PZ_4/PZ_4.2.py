
try:
    N = int(input("Введи целое число N (>0), которое равно 2^K: "))
    if N <= 0:
        print("N должно быть больше нуля.")
    else:
        K = 0
        temp = N
        # Проверим, что N - степень двойки и найдём K
        while temp != 1:
            if temp % 2 != 0:
                print("N не является степенью числа 2.")
                break
            temp //= 2
            K += 1
        else:
            print("Показатель степени K =", K)
except ValueError:
    print("Ошибка: ввод должен быть целым числом.")
