# Дан список X, состоящий из целых чисел и целое число b. Исключить из списка элементы, равные b.
# Ввод: X = [3, 0, 7, 0, 0, 3]; b = 3
# Вывод: [0, 7, 0, 0]

# Ввод данных
a = input("Пожалуйста, введите любую последовательность целых чисел: ")
b = input("Пожалуйста, введите целое число, которое необходимо исключить: ")
# Проверка ввода
if not a.isdigit:
    print("Некорректный ввод.")
    exit(1)
if not b.isdigit:
    print("Некорректный ввод.")
    exit(1)

no_spacebar = a.replace(" ", "")
numbers = no_spacebar.split(',')  # numbers - список

# Исключение b
result = []
for i in numbers:
    if i != b:
        result.append(i)
print(result)
