print("break used here")
for i in range(1,11):
    if i==5:
        break
    print(i)                     #Break

print("continue")
s="string"
for n in s:
    if n=="i":
        continue
    print(n)                  #Continue

print("pass")  
for i in range(1,11):
    if i%2==0:
        pass
    else:
        print(i)               #Pass

print("for with else")
for i in range(1,11):
     if i%2==0:
         print(i," is even")
     else :
         print(i," is odd")             #For else

print("while with else")
i=1
while i<=10:
     if i%2==0:
         print(i," is even")
         i+=1 
     else:
         print(i," is odd")         #While with else
         i+=1          
              