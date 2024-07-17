def sum(x,y):
    c = x+y
    return(c)

def substraction(x,y):
    c = x-y
    return(c)

def multiplication(x,y):
    c = x*y
    return(c)

def division(x,y):
    c = x/y
    return(c)

print("select your operation :")
print("1.sum")
print("2.substraction")
print("3.multiplication")
print("4.division")
while True:
   select = int(input("enter your choice :"))
   num1 = int(input("enter a number :"))
   num2 = int(input("enter a number :"))

   if select ==1:
    print(num1, "+", num2, "=" ,sum(num1,num2))
   elif select ==2:
    print(num1, "-", num2, "=", substraction(num1, num2))
   elif select ==3:
    print(num1, "*", num2, "=", multiplication(num1, num2))
   elif select ==4:
    print(num1, "/", num2, "=", division(num1, num2))
   else:
    print("syntax error")
