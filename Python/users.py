import os
print("****** Add Users ******")
users = []
while True:
  id = int(input("Enter user id: "))
  name  = str(input("Enter user name: "))
  role = str(input("Enter user role: "))
  sallary = str(input("Enter user sallary: "))
    

  filename = "employee.pdf"
  i = 1
  if not os.path.exists(filename):
      print(f" {filename} file not found!")
  else:
      file = open(filename, "a")
      file.write(f"ID : {id} \n")
      file.write(f"Name : {name} \n")
      file.write(f"Email : {role} \n")
      file.write(f"Sallary : {sallary} \n\n")
      i += 1
      file.close()

      

 
  userData = { "name": name, "role": role, "sallary": sallary }
  users.append(userData)

  option = str(input("Continue (y/n)? "))
  if option == "n":
    break




print("****** User List ******")
print(users)


