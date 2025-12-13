# Вариант 15
# Дано трехзначное число. Вывести в начале его последнюю цифру,
# (единицы), а затем - его среднюю цифру (десятки)
while True:  
    try:
        number = int(input('Введите трехзначное число: '))  

        if 100 <= number <= 999:  
            last_number = number % 10  
            middle_number = (number // 10) % 10  
            print(f'Результат: {last_number}, {middle_number}') 
            break  
        else:
            print('Неверный ввод. Попробуйте снова')  

    except ValueError:
        print('Неверный ввод. Попробуйте снова')