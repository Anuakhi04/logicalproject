num = int(input('enter the number of elements: '))
num1 = []
for i in range(num):
    y = int(input("enter the value: "))
    num1.append(y)
print(num1)
# num1=[1,9,8,5,4]
for n in range(1,max(num1)):
    if n not in num1:
        print(n)
        break
