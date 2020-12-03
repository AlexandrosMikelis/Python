import abc
import time
import Decorators
class User:
    def __init__(self,name,surname,nickname,email,password):
        self.name = name
        self.surname = surname
        self.nickname = nickname
        self.email = email
        self.password = password

class Validate(User):
    logpathcheck,IsLoggedIn,IsRegistered = 0,0,0
    def __init__(self,name,surname,nickname,email,password):
        super().__init__(name,surname,nickname,email,password)
        UserDB = open("UserDB.txt" , "r")
        for Users in UserDB :
            info = Users.split(" ")
            if self.email == info[0] and self.password == info[1] :
                Validate.IsLoggedIn = 1
                self.name = info[2]
                self.surname = info[3]
                self.nickname = info[4][:-1]
                break
            elif self.email == info[0] :
                Validate.IsRegistered = 1
                break
            Validate.IsRegistered = 0
            
class Login(Validate): 
    
    def __init__(self,name,surname,nickname,email,password):
        super().__init__(name,surname,nickname,email,password)
    
    def ResetPassword(self,newPassword):
        newDB = []
        UserDB = open("UserDB.txt" , "r+")
        for Userss in UserDB :
            info = Userss.split(" ")
            if(info[0]!=self.email):
                newDB.append(Userss)
            else:
                newDB.append(self.email + " " + newPassword + " " + self.name 
                             + " " + self.surname + " "+ self.nickname +"\n")
        UserDB.seek(0)
        for i in newDB:
            UserDB.write(i)
        UserDB.close()
    
    def Delete(self):
        UserDB = open("UserDB.txt" , "r+")
        if(Validate.IsLoggedIn == 1):
            lines = UserDB.readlines()
            UserDB.seek(0)
            for i in lines:
                if i != self.email + " " + self.password + " " + self.name + " " + self.surname + " "+ self.nickname +"\n":
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
            
    @Decorators.timeit
    def Logout(self,StartTime):
        print("You logged out")
        Validate.IsLoggedIn,Validate.IsRegistered =0,0
    
class Register(Validate):
    def __init__(self,name,surname,nickname,email,password):
        super().__init__(name,surname,nickname,email,password)
        
    def UserRegister(self):
        if(Validate.IsRegistered == 0):
            UserDB = open("UserDB.txt" , "a")
            if(self.password.isalpha() or
               self.password.isdigit() or
               self.password.islower() or
               self.password.isupper()):
                print("""\n!!!Your password need to have at least one alphabetic 
                      , digit , lower and a capital character!!!\n""")
            else:
                UserDB.write(self.email + " " + self.password + " " + self.name 
                             + " " + self.surname + " "+ self.nickname +"\n")
                Validate.IsRegistered = 1
                print("\nYou are now registered\n")
            UserDB.close()
        else:
            print("\nYou are already Registered\n")

class BaseUser(Login,Register,metaclass=abc.ABCMeta):

    pass
    # @abc.abstractmethod
    # def Characteristics(self):
    #     print('YO')
        
        
    
    # @abc.abstractmethod    
    # def SessionTime(self):
    #     print("No")
    #     pass
    
class SimpleUser(BaseUser,metaclass=abc.ABCMeta):
    def __init__(self,name,surname,nickname,email,password):
        super().__init__(name,surname,nickname,email,password)
    @Decorators.newChars
    def Characteristics(self):
        print("========================")
        print("|You are simple User   |")
        print("========================")
    
    def SessionTime(self,startTime):
        start = startTime
        end = time.time()
        return end - start

class StaffUser(BaseUser,metaclass=abc.ABCMeta):
    def __init__(self,name,surname,nickname,email,password):
        super().__init__(name,surname,nickname,email,password)
    @Decorators.newChars
    def Characteristics(self):
        print("========================")
        print("|You are Staff User    |")
        print("========================")
    
    def UsersDisplay(self):
        UserDB = open("UserDB.txt" , "r")
        for Users in UserDB :
            print(Users)
        
    def Warn(self,Email):
        UserDB = open("UserDB.txt" , "r")
        for Users in UserDB :
            info = Users.split(" ")
            if self.email == info[0] :
                print("Sending Warning to {}".format(Email))
        
class AdminUser(BaseUser,metaclass=abc.ABCMeta):
    def __init__(self,name,surname,nickname,email,password):
        super().__init__(name,surname,nickname,email,password)
    @Decorators.newChars
    def Characteristics(self):
        print("========================")
        print("|You are Admin User    |")
        print("========================")
    
    def UsersDisplay(self):
        UserDB = open("UserDB.txt" , "r")
        for Users in UserDB :
            print(Users)
        
    def Warn(self,Email):
        UserDB = open("UserDB.txt" , "r")
        for Users in UserDB :
            info = Users.split(" ")
            if self.email == info[0] :
                print("Sending Warning to {}".format(Email))
                
    def Ban(self,Email):
        UserDB = open("UserDB.txt" , "r")
        for Users in UserDB :
            info = Users.split(" ")
            if self.email == info[0] :
                print("Banning {}".format(Email))
        