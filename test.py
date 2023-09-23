x = 8


def bla(x):
    print("before: ", x)
    x = 11
    print("after: ", x)


bla(7)

bla(x)

print("outside: ", x)
