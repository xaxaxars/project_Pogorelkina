with open("text18-15.txt", "r", encoding="utf-8") as f:
    text = f.read()


print("Содержимое файла:")
print(text)


small_letters = sum(1 for char in text if char.islower() and char.isalpha())
print(f"\nБукв в нижнем регистре: {small_letters}")


with open("text18-15_STIH.txt", "w", encoding="utf-8") as f:
    f.write(text.upper())

print("Создан файл text18-15_STIH.txt с текстом в верхнем регистре")


with open("text18-15_STIH.txt", "r", encoding="utf-8") as f:
    print("\nНовый файл:")
    print(f.read())