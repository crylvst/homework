# Дан список любых целых чисел. Исключить из него максимальный и минимальный элемент.
# Ввод данных
a = input("Пожалуйста, введите список чисел: ")

# Проверка ввода, удаление лишних элементов списка
if not a.isdigit:
    print("Некорректный ввод.")
    exit(1)

no_spacebar = a.replace(" ", "")
numbers = no_spacebar.split(',')
print(numbers)  # для наглядности работы кода
numcopy = numbers.copy()  # для корректной работы алгоритма с минимальным элементом

# Исключение максимального элемента
MAX_num = max(numbers, key=int)
numbers.remove(MAX_num)
print(numbers)

# Исключение минимального элемента
MIN_num = min(numcopy, key=int)
numcopy.remove(MIN_num)
print(numcopy)

# Вариант с упорядочиванием и удалением наибольшего элемента:
# numlistMAX = sorted(numbers, key=int)
# del numlistMAX[-1]
# print(numlistMAX)

# Вариант с упорядочиванием и удалением наименьшего элемента:
# numlistMIN = sorted(numbers, key=int, reverse=True)
# del numlistMIN[-1]
# print(numlistMIN)

# Лично мне вариант с упорядочиванием нравится больше!
