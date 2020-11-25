class User:
    def __init__(self,name,surname,nickname,email,password):
        self.name = name
        self.surname = surname
        self.nickname = nickname
        self.email = email
        self.password = password

class Validate(User):
    logpathcheck,IsLoggedIn,position,IsRegistered = 0,0,0,0
    def __init__(self,name,surname,nickname,email,password):
        super().__init__(name,surname,nickname,email,password)
        UserDB = open("UserDB.txt" , "r")
        for Users in UserDB :
            Validate.position = Validate.position + 1
            info = Users.split(" ")
            if self.email == info[0] and self.password == info[1][:-1] :
                Validate.IsLoggedIn = 1
                break
            elif self.email == info[0] :
                print("here")
                Validate.IsRegistered = 1
                break
class Login(Validate):   
    def ResetPassword(self,newPassword):
        UserDB = open("UserDB.txt" , "r+")
        content = UserDB.readlines()
        content[Validate.position - 1] = self.email + " " + newPassword + "\n"
        UserDB.seek(0)
        for i in content:
            UserDB.write(i)
        UserDB.close()
    def Delete(self):
        UserDB = open("UserDB.txt" , "r+")
        if(Validate.IsLoggedIn == 1):
            lines = UserDB.readlines()
            UserDB.seek(0)
            for i in lines:
                if i != self.email + " " + self.password + "\n":
                    UserDB.write(i)
            UserDB.truncate()
            Validate.IsLoggedIn=0
            Validate.IsRegistered =0
            Validate.position = 0
            Validate.logpathcheck = 0
        UserDB.close()
    def LogIn(self):
        if( Validate.IsLoggedIn == 0 ):
            Validate.IsLoggedIn = 1
            if (Validate.IsRegistered == 1):
                print("Wrong Password Try Again")
            else:
                print("\nYou need to Register First\n")
        else:
            Validate.logpathcheck =1
            print("\nYou logged in Successfully\n")
    def Logout(self):
        Validate.IsLoggedIn,Validate.position,Validate.IsRegistered =0,0,1
    
class Register(Validate):
    def Reg(self):
        print( self.name + " " + self.surname + " registered succesfully")
    def UserRegister(self):
        if(Validate.IsRegistered == 0):
            UserDB = open("UserDB.txt" , "a")
            if(self.password.isalpha() or self.password.isdigit() or self.password.islower() or self.password.isupper()):
                print("\n!!!Your password need to have at least one alphabetic , digit , lower and a capital character!!!\n")
            else:
                UserDB.write(self.email + " " + self.password + "\n")
                Validate.IsRegistered = 1
                print("\nYou are now registered\n")
            UserDB.close()
        else:
            print("\nYou are already Registered\n")
class UserManager(Login,Register):
    def Manage(self):
        if(self.email[-12:-3]=="dataverse"):
            print("========================")
            print("|You are premium Member|")
            print("========================")
        else:
            print("You are simple User")
    
