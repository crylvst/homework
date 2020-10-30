# Дан список X и число A. Вычислить сумму всех отрицательных элементов списка Х, значения которых больше, чем A.
# Подсчитать также количество таких элементов.
# Ввод: X = [-3, 5, -7, -4, -2, 13]; A = -4
# Вывод:
# -5
#  2

# Ввод
x = input("Пожалуйста, введите последовательность чисел: ")
a = int(input("Пожалуйста, введите число: "))

if not x.isdigit:
    print("Некорректный ввод.")
    exit(1)
no_spacebar = x.replace(" ", "")
numbers = no_spacebar.split(',')  # numbers - список
nums = [int(item) for item in numbers]

# Решение
spisok = []
for i in nums:
    if i > a and i < 0:
        spisok.append(i)
print(sum(spisok))
print(len(spisok))