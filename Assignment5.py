num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))
num3 = int(input("Enter third number: "))
num4 = int(input("Enter fourth number: "))
num5 = int(input("Enter Fiveth number: "))

l1=[num1,num2,num3,num4,num5]
print(l1)

#1)Sum of all numbers
print("sum: ",sum(l1))

#2)Smallest number 
print("Smallest: ",min(l1))

#3)Largest number
print("Largest",max(l1))

#4)Ascending order
l1.sort()
print("Sort Ascending: ",l1)

#5)Descending order
l1.sort(reverse=True)
print("Sort Descending: ",l1)

#6)Convert list to tuple
t=()
t=tuple(l1)
print("tuple: ",t)

#7)Delete the list
del l1
print(l1)