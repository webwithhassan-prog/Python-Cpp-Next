class Student:
    def __init__(self , email , passw ):
        self.email   = email
        self.passw   = passw

    def get_credentials(self):
        return  self.email , self.passw 
    
    def set_credentials(self , email , passw ):
        self.email = email
        self.passw = passw
        

u_email = str(input("Enter Your Email :"))        
u_passw = str(input("Enter Pass :"))        
student = Student(u_email,u_passw)
student.set_credentials(u_email,u_passw)
user_cred = student.get_credentials()

print(user_cred)

