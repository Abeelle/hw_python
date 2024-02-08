def simp(x:int)->bool:
    result=True
    for i in range (2,x):
        if x%i==0:
            result=False
        break
    return (result)
print(simp(10))