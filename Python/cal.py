import calLib
#inputs 
n1  = int(input("Enter 1st Number : "))
n2  = int(input("Enter 2nd Number : "))
opr = str(input("Enter operator : "))

if opr == "+":
    calLib.add(n1,n2)
elif opr == "-":
    calLib.subs(n1,n2)
elif opr == "/":
    calLib.divide(n1,n2)
elif opr == "*":
    calLib.multi(n1,n2)
else:
    print("wrong operator")
    