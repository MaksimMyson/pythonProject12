line = input("Введите строку: ")
line = line.replace(" ", "").upper()
if line == line[::-1]:
    print("Палиндром")
else:
    print("Не палиндром")


