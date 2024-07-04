def sum_add(x):
    if x==1:
        return 1
    return x+sum_add(x-1)
result=sum_add(5)
print(result)