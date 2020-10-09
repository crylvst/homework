# Ввод данных
a = str(input("Пожалуйста, введите градусы в формате 12C или 2.5F: "))

# Проверка ввода данных
digits = "-0123456789"
if a[0] not in digits:
    print("Неверный ввод.")
    exit(1)
degree = "CcFf"
if a[-1] not in degree:
    print("Неверный ввод.")
    exit(1)
alphabet = "abcdefghijklmnopqrstuvwxyz"
if a[0:-1] in alphabet:
    print("Неверный ввод.")
    exit(1)

# Формирование ответа
b = float(a[0:-1])
if a[-1] in "Cc":
    f = (b * 1.8) + 32
    print("Результат: ", round(f, 2), "F")
elif a[-1] in "Ff":
    c = (b - 32) / 1.8
    print("Результат: ",  round(c, 2), "C")
