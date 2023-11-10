# для начала выводим алгоритм, который позволит понять закономерность и расположение цветов доски.
# Если координаты равны, то всегда будет чёрная клеточка. Но если одна из координат чётная, а другая нечётная,
# то координата всегда белая. Также, если обе координаты чётные или нечётные, то клеточка чёрная. Тогда, пусть
# чётная координата-это 1(true), а нечётная координата-это 0(false).
# Получается, что если обе координаты чётные или нечётные,то в сумме (0+1) будут равны 1, т.е. будет белая клетка.
# Если обе координаты чётные или нечётные, то в сумме будут давать 2 или 1.



def whatColour(a, b):
    if a == b:
        return "B"
    xColour = int(a % 2 == 0)
    yColour = int(b % 2 == 0)
    sumC = xColour + yColour
    if sumC == 1:
        return "W"
    if sumC == 0 or sumC == 2:
        return "B"

def doTest():
    if "B" == whatColour(6, 4):
        print("OK, 6,4=B")

    if "W" == whatColour(4, 7):
        print("OK, 4,7=W")

    if "B" == whatColour(7, 5):
        print("OK, 7,5=B")

    if "B" == whatColour(4, 6):
        print("OK, 4,6=B")


x1,y1=int( input("x1")) , int(input("y1") )
x2,y2=int(input("x2")),int(input("y2"))

cell1=whatColour(x1,y1)
cell2=whatColour(x2,y2)
if cell1==cell2:
    print("cells have same colours", cell1)
else:
    print("cells have different colours. cell1= ",cell1, " cell2=",cell2)
