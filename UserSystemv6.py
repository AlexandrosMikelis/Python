import abc
import Decorators

class Validate:
    
    def __init__(self,name,surname,nickname,email,password):
        
        self.name = name
        self.surname = surname
        self.nickname = nickname
        self.email = email
        self.password = password
        self.logpathcheck = 0
        self.IsLoggedIn = 0
        self.IsRegistered = 0
        
        
        UserDB = open("UserDB.txt" , "r")
        for Users in UserDB :
            info = Users.split(" ")
            if self.email == info[0] and self.password == info[1] :
                
                self.IsLoggedIn = 1
                self.IsRegistered = 1
                self.name = info[2]
                self.surname = info[3]
                
                try:
                    
                    if info[5] != '':
                        self.nickname=info[4]
                        
                except:
                    
                    self.nickname = info[4][:-1]
                    
                break
            
            elif self.email == info[0] :
                
                self.IsLoggedIn = 0
                self.IsRegistered = 1
                break
            
            self.IsRegistered = 0
            self.IsLoggedIn = 0
            
class Login(Validate): 
    
    def __init__(self,name,surname,nickname,email,password):
        super().__init__(name,surname,nickname,email,password)
    
    def ResetPassword(self,newPassword):
        newDB = []
        self.password = newPassword
        UserDB = open("UserDB.txt" , "r+")
        for Userss in UserDB :
            info = Userss.split(" ")
            if(info[0]!=self.email):
                newDB.append(Userss)
            else:
                if(info[-1][:-1] == self.nickname or info[-2] == self.surname):
                    newDB.append(self.email + " " 
                                 + newPassword + " " 
                                 + self.name + " "
                                 + self.surname + " " 
                                 + self.nickname + "\n")
                else:
                    newDB.append(self.email + " " 
                                 + newPassword + " " 
                                 + self.name + " "
                                 + self.surname + " " 
                                 + self.nickname + " " 
                                 + info[-2] +" "
                                 + info[-1][:-1] + '\n')
                    
        UserDB.seek(0)
        for i in newDB:
            UserDB.write(i)
        UserDB.close()
        return "Your Successfully Changed Your Password"
    
    def Delete(self):
        with open("UserDB.txt" , "r+") as f:
            new_f = f.readlines()
            f.seek(0)
            for line in new_f:
                if self.email not in line:
                    f.write(line)
            f.truncate()
        self.IsLoggedIn=0
        self.IsRegistered =0
        self.logpathcheck = 0
    
    def LogIn(self):
        if( self.IsLoggedIn == 0 ):
            self.IsLoggedIn = 1
            if (self.IsRegistered == 1):
                return "Wrong Password Try Again"
            else:
                self.IsLoggedIn = 0
                return "\nYou need to Register First\n"
        else:
            self.logpathcheck =1
            return "\nYou logged in Successfully\n"
            
    @Decorators.timeit
    def Logout(self,StartTime):
        self.IsLoggedIn,self.IsRegistered,self.logpathcheck =0,0,0
        return "You logged out"
    
class Register(Validate):
    def __init__(self,name,surname,nickname,email,password):
        super().__init__(name,surname,nickname,email,password)
        
    def UserRegister(self):
        if(self.IsRegistered == 0):
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
                self.IsRegistered = 1
                return "\nYou are now registered\n" 
            
            UserDB.close()
        else:
            print("\nYou are already Registered\n")

class BaseUser(Login,Register,metaclass=abc.ABCMeta):
    
    @abc.abstractmethod
    def Characteristics(self):
        pass
        
    
class SimpleUser(BaseUser,metaclass=abc.ABCMeta):
    
    def __init__(self,name,surname,nickname,email,password):
        super().__init__(name,surname,nickname,email,password)
        
    @Decorators.newChars
    def Characteristics(self):
        
        print("="*23)
        print("|You are simple User   |")
        print("="*23)
    
class StaffUser(BaseUser,metaclass=abc.ABCMeta):
    def __init__(self,name,surname,nickname,email,password):
        super().__init__(name,surname,nickname,email,password)
        
    @Decorators.newChars
    def Characteristics(self):
        
        print("========================")
        print("|You are Staff User    |")
        print("========================")
        
    @Decorators.UserShowcase
    def UsersDisplay(self):
        pass
        
    def Warn(self,Email):
        
        UserDB = open("UserDB.txt" , "r")
        for Users in UserDB :
            info = Users.split(" ")
            if self.email == info[0] and self.email[-12:-3]!= 'dataverse':
                print("Sending Warning to {}".format(Email))
        
class AdminUser(BaseUser,metaclass=abc.ABCMeta):
    def __init__(self,name,surname,nickname,email,password):
        super().__init__(name,surname,nickname,email,password)
        
    @Decorators.newChars
    def Characteristics(self):
        
        print("========================")
        print("|You are Admin User    |")
        print("========================")
        
    @Decorators.UserShowcase
    def UsersDisplay(self):
        pass
        
    def Warn(self,Email):
        
        UserDB = open("UserDB.txt" , "r")
        for Users in UserDB :
            info = Users.split(" ")
            if (self.email == info[0] and 
                self.email[-12:-3]!= 'dataverse' and 
                self.email[0:5] != "admin"):
                
                print("Sending Warning to {}".format(Email))
                
    def Ban(self,Email):
        
        UserDB = open("UserDB.txt" , "r")
        for Users in UserDB :
            info = Users.split(" ")
            if self.email == info[0] :
                return "Banning {}".format(Email) 
        