def add(a,b):
    return a+b
def subtract(a,b):
    return a-b
def multiply(a,b):
    return a*b
def divide(a,b):
    if b!= 0:
     return a/b
    else:
        return "can't divide by Zero"
def modulo(a,b):
    if b!=0:
     return a%b
    else:
        return "can't perform modulo by Zero"
def power(a,b):
    return a**b
num1 = float(input("Enter first number:"))
num2 = float(input("Enter second number:"))
print("choose operation:")
print("1.Addition")
print("2.Subtraction")
print("3.Multiplication")
print("4.Division")
print("5.Modulo")
print("6.Power")
choice = int(input("Enter choice (1/2/3/4/5/6): "))
if choice == 1:
    print("Result: ", add(num1,num2))
elif choice == 2:
    print("Result: ", subtract(num1,num2))
elif choice == 3:
    print("Result: ", multiply(num1,num2))
elif choice == 4:
    print("Result: ", divide(num1,num2))
elif choice == 5:
    print("Result: ", modulo(num1,num2)) 
elif choice == 6:
    print("Result: ", power(num1,num2))

