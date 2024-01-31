def minn (numbers:list)->int:
    min=float("inf")
    for i in numbers:
        if i %3==0:
            if i < min:
                min=i
    return min
numbers=[1,2,4,5,6]
print(minn(numbers))