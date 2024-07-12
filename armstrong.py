
num = int(input("Enter the number: "))
sum = 0
a = num
order = len(str(num))

while a > 0:
    number = a % 10
    sum += number ** order
    a = a // 10
if num == sum:
    print(num, "is an Armstrong number.")
else:
    print(num, "is not an Armstrong number.")

