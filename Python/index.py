print("Sum and Average of Subject Marks")
eng = int(input("Enter Enslish Marks Out of 100 : "))
urdu = int(input("Enter Urdu Marks Out of 100 : "))
math = int(input("Enter Math Marks Out of 100 : "))
isl = int(input("Enter Islamiyat Marks Out of 100 : "))
phy = int(input("Enter Physics Marks Out of 100 : "))

sum = eng + urdu + math + isl + phy
avg = sum/5

print("Sum of all objects : " , sum)
print("Average : " , avg)