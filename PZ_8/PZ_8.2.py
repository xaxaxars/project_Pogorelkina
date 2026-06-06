# Сгенерировать словарь вида {0: 0, 1: 1, 2: 4, 3: 9, 4: 16, 5: 25, 6: 36}, удалить из него
# второй и третий элементы. Отобразить исходный и получившийся словарь.
original_dict = {i: i**2 for i in range(7)}
print("Исходный словарь:", original_dict)

new_dict = original_dict.copy()

for key in [1, 2]:
    if key in new_dict:
        del new_dict[key]

print("Получившийся словарь:", new_dict)