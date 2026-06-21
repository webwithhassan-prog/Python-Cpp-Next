users = []

while True:
    userName = input("Enter User name : ")
    userEmail = input("Enter User email : ")
    userPass = input("Enter User pass : ")

    userData = {
        "name": userName,
        "email": userEmail,
        "passw": userPass
    }

    users.append(userData)

    option = input("Continue (y/n)? ")
    if option == "n":
        break

print("\n ----User List----")
i = 1
for user in (users):
    print(f"User no {i} ")
    print(f"id       : {i} ")
    print(f"Name     : {user['name']}")
    print(f"Email    : {user['email']}")
    print(f"Password : {user['passw']}")
    i += 1
    