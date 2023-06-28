num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))
opr = input("Select operation: +, -, *, /,%,//,** \n")

if opr == "+":
    print(num1, "+", num2, "=", num1+num2)

elif opr == "-":
    print(num1, "-", num2, "=", num1-num2)

elif opr == "*":
    print(num1, "*", num2, "=", num1*num2)

elif opr == "/":
    print(num1, "/", num2, "=", num1/num2)

elif opr == "%":
    print(num1, "%", num2, "=", num1%num2)

elif opr == "//":
    print(num1, "//", num2, "=", num1//num2)

elif opr == "**":
    print(num1, "**", num2, "=", num1**num2)
    
else:
    print("Invalid input")