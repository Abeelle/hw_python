import math
def findSandP():
    a=int(input("введите сторону а="))
    b=int(input("введите сторону b="))
    c=int(input("введите сторону c="))
    if a+b>c and a+c>b and b+c>a:
        P=a+b+c
        p=P/2
        S=math.sqrt(p*(p-a)*(p-b)*(p-c))
        print("P=",P,"S=",S)
    else:
        print("такого треугольника не сущеcтвует")

findSandP()


