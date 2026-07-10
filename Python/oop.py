userList = []

class User:
    name = "Usman"
    age = 44
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def information(self):
        print(f"My name is {self.name} and my age is {self.age}")

u1 = User("Ali",12)

u1.information()