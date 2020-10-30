# Дан список из любых целых чисел, в котором есть два нулевых элемента. Исключить нулевые элементы.
# Ввод данных
a = input("Пожалуйста, введите любую последовательность чисел, включающую нули (как минимум больше двух нулей): ")

# Проверка ввода и удаление лишних элементов списка
if not a.isdigit:
    print("Некорректный ввод.")
    exit(1)

no_spacebar = a.replace(" ", "")
numbers = no_spacebar.split(',')  # numbers - список
# print(numbers)  # для наглядности списка
y = numbers.count("0")
# print(y)  # для наглядности подсчёта нолей в списке

if y == 0 or y == 1:
    print("Неверный ввод.")
    exit(1)

# Выведение списка без нолей
result = []
for i in numbers:
    if i != "0":
        result.append(i)
print(result)
