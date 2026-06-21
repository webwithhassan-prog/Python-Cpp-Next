savedPass = "0000"
passCount = 0
while True:
 passw = str(input("Enter Password : "))
 passCount += 1 
 if len(passw) != 4:
   print("-----Enter only 4 digits password-----")
 if passw != savedPass:
   print(f"-----You tried password {passCount} times-----")
   print("-----You have entered Wrong Password-----")
 if passCount >= 3 and passw != savedPass :
    print("-----Try again after 30 secs-----")
 print("----------------------------------------------------")
 if passw == savedPass:
  print(f"-----Password Matched Finally After {passCount} tries !!!-----")
  break

print("----------------------------------------------------")