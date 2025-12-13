
# Функция, которая выводит на экран строку из заданного количества символов

def print_string(length):
    s = input("Введите символы для вывода: ")
    # Если введённая строка длиннее нужной длины, обрежем её
    if len(s) > length:
        s = s[:length]
    # Если короче, дополним пробелами
    elif len(s) < length:
        s = s + " " * (length - len(s))
    print(s)

while True:
    try:
        n = int(input("Введите количество символов в строке: "))
        if n > 0:
            break
        else:
            print("Введите число больше нуля.")
    except ValueError:
        print("Неправильно ввели! Попробуйте ещё раз.")

print_string(n)
