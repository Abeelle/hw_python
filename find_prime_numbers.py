x=int(input())
result=True
for i in range(2,x):
    if x%i==0:
        print("yes")
        result=False
        break
print(result)




