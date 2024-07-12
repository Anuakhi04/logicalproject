num = int(input("enter a number :"))
a=0
b=1
for i in range(num):
    print(a,end=" ")
    # a,b=b,a+b
    c=a+b
    a=b
    b=c
print()