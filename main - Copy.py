from assignment_9 import MyMathModule, MyException

try:
    num = int(input("Enter a number: "))
    m = MyMathModule(num)
    
    print("Square:", m.square())
    print("Square Root:", m.square_root())
    print("Factorial:", m.factorial())
    print("Logarithm:", m.logarithm())
    
    if num == 0:
        raise MyException("Number cannot be zero!")
    
except ValueError:
    print("Invalid input. Please enter a valid number.")
    
except MyException as e:
    print("Exception:", str(e))
