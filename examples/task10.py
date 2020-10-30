# Вывести все элементы списка, стоящие до максимального элемента этого списка
# Ввод: X = [3, 0, 7, 0, 0, 3]
# Вывод: [3, 0]

# Ввод данных
a = input("Пожалуйста, введите последовательность цифр: ")

# Проверка
if not a.isdigit:
    print("Некорректный ввод.")
    exit(1)
no_spacebar = a.replace(" ", "")
numbers = no_spacebar.split(',')  # numbers - список

# Решение
MAX_num = max(numbers, key=int)
y = numbers.index(MAX_num)

print(numbers[:y])
