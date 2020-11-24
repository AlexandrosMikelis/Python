class User:
    def __init__(self,name,surname,nickname,email,password):
        self.name = name
        self.surname = surname
        self.nickname = nickname
        self.email = email
        self.password = password

class Validate(User):
    def __init__(self,name,surname,nickname,email,password,IsLoggedIn,position,IsRegistered):
        super().__init__(name,surname,nickname,email,password)
        UserDB = open("UserDB.txt" , "r")
        self.position = 0
        self.IsLoggedIn = 0
        self.IsRegistered = 0
        for Users in UserDB :
            self.position = self.position + 1
            info = Users.split(" ")
            if self.email == info[0] and self.password == info[1][:-1] :
                self.IsLoggedIn = 1
                break
            elif self.email == info[0] :
                self.IsRegistered = 1
                break
class Login(Validate):
    def ResetPassword(self,newPassword):
        UserDB = open("UserDB.txt" , "r+")
        content = UserDB.readlines()
        content[self.position - 1] = self.email + " " + newPassword + "\n"
        UserDB.seek(0)
        for i in content:
            UserDB.write(i)
        UserDB.close()
    def Delete(self):
        UserDB = open("UserDB.txt" , "r+")
        if(self.IsLoggedIn == 1):
            lines = UserDB.readlines()
            UserDB.seek(0)
            for i in lines:
                if i != self.email + " " + self.password + "\n":
                    UserDB.write(i)
            UserDB.truncate()
            self.IsLoggedIn=0
            self.IsRegistered =0
            self.position = 0
        UserDB.close()
    def LogIn(self):
        if( self.IsLoggedIn == 0 ):
            self.IsLoggedIn = 1
            print("You need to Register First")
        else:
            print("You logged in Successfully")
    
class Register(Validate):
    def Reg(self):
        print( self.name + " " + self.surname + " registered succesfully")
    def UserRegister(self):
        if(self.IsRegistered == 0):
            UserDB = open("UserDB.txt" , "a")
            if(self.password.isalpha() or self.password.isdigit() or self.password.islower() or self.password.isupper()):
                print("Your password need to have at least one alphabetic , digit , lower and a capital character!!!")
            else:
                UserDB.write(self.email + " " + self.password + "\n")
                self.IsRegistered = 1
                print("You are now registered")
            UserDB.close()
        else:
            print("You are already Registered")

class Admin(Login,Register,Validate):
    def Identity(self):
        print("User: " + self.nickname + " Position : Admin")
class SimpleUser(Login,Register,Validate):
    def Identity(self):
        print("User: " + self.nickname + " Position : SimpleUser")
