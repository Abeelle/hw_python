year = (("Январь", 31), ("Февраль", 28), ("Март", 31), ("Апрель", 30), ("Май", 31), ("Июнь", 30),
        ("Июль", 31), ("Август", 31), ("Сентябрь", 30), ("Октябрь", 31), ("Ноябрь", 30), ("Декабрь", 31))

x = int(input("Введи номер месяца:"))

if 0 < x <= 12:
    print("Месяц:", year[x - 1][0], "Дни:", year[x - 1][1])
else:
    print("На этой планете нет такого месяца")
