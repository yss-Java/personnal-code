# num=int(input())
# for i in range(0,10):
#     print(i)


num=int(input())
result =0
src=num
while num != 0:
   result+=(num%10)**3
   num//=10
if result==src:
    print(src,"是水仙花数")

else:
    print(src,"不是水仙花数")