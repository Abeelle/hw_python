x1 = -4
y1 = 1
x2 = -4
y2 = 4
x3 = 2
y3 = 4


# она одну переменную, которая отлична от двух других, при этом другие равны
def findhonest(a1, a2, a3):
    if a1 == a2:
        return a3
    elif a2 == a3:
        return a1
    else:
        return a2


def findlostpoint(x1, y1, x2, y2, x3, y3):
    y4 = findhonest(y1, y3, y2)
    x4 = findhonest(x1, x3, x2)
    print(x4, y4)


findlostpoint(x1, y1, x2, y2, x3, y3)
