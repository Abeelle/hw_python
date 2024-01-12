def findprimenum(x):
    result=True
    for i in range(2,x):
        if x%i==0:
            result=False
        break
    return(result)

print(findprimenum(7))






