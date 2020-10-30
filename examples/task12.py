# Дан список чисел. Вычислить среднее арифметическое положительных элементов этого списка
# и среднее арифметическое отрицательных элементов этого списка (0 исключать, он ни положителен, ни отрицателен)
# Ввод: X = [-3, 5, -7, -4, -2, 13, 0]
# Вывод:
# -4
# 9

# Ввод
a = input("Пожалуйста, введите последовательность чисел: ")

# Проверка ввода и удаление лишних элементов списка
if not a.isdigit:
    print("Некорректный ввод.")
    exit(1)

no_spacebar = a.replace(" ", "")
numbers = no_spacebar.split(',')  # numbers - список
nums = [int(item) for item in numbers]

# Решение
plus = []
minus = []
for i in nums:
    if i > 0:
        plus.append(i)
resultPLUS = sum(plus) / len(plus)
print(resultPLUS)

for _ in nums:
    if _ < 0:
        minus.append(_)
resultMIN = sum(minus) / len(minus)
print(resultMIN)
