operator = input("Enter an operator: ") 
num1 = input("Enter the first number: ")
num2 = input("Enter the second number: ")

if operator == "+":
    print(num1+num2)
elif operator == "-":
    print(num1 - num2)
elif operator == "/":
    print(num1 / num2)
elif operator == "*":
    print(num1 * num2)
else:
    print("Error 101")