#


def max_number():
    x = [11, 6, 42]
    max = x[0]
    for i in x:
        if i > max:
            max = i
    print(max)


def even_and_odd(x_param):
    if x_param % 2 == 0:
        print(x_param)
    else:
        print("false")


def last_number():
    x = int(input(":-> "))
    i = x % 10
    print(i)


def last_number_noinput(x):
    x = int(x)
    i = x % 10
    print(i)


max_number()

even_and_odd(3)

last_number_noinput(12765)

last_number()
