# Функция вычисляет, на сколько квадратов разрезать прямоугольник A x B,
# отрезая каждый раз квадрат наибольшей стороны.

def count_squares(A, B):
    count = 0
    while A != 0 and B != 0:
        if A > B:
            count += A // B
            A = A % B
        else:
            count += B // A
            B = B % A
    return count

while True:
    try:
        A = int(input("Введите длину стороны A (натуральное число): "))
        B = int(input("Введите длину стороны B (натуральное число): "))
        if A > 0 and B > 0:
            break
        else:
            print("Введите натуральные числа больше нуля.")
    except ValueError:
        print("Неправильно ввели! Попробуйте ещё раз.")

result = count_squares(A, B)
print("Можно разрезать на", result, "квадратов")
