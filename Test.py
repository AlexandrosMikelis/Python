# -*- coding: utf-8 -*-
"""
Created on Mon Dec  7 11:34:58 2020

@author: Alex
"""
#iamalekos@hotmail.com Hello1234 alex mikelis mika 2020-12-04 13:07:48.421607
import UserSystemv6 as Users
import time 

def DatabaseSearch(User):
    UserDB = open("UserDB.txt" , "r+")
    for Userss in UserDB :
        info = Userss.split(" ")
        if (info[0] == User.email and info[1] == User.password and 
            info[2] == User.name and info[3] == User.surname and 
            info[4] == User.nickname ):
            return 1
    return 0


starttime = 0
validuser = 0
Email = "Example@gmail.com"
newPassword = "newPassword123"


class TestClass:
    def test_UserPath0(self):
        """ UserPath3 : 
                  Register
            Note:
                Available for exery User
        """
        user = Users.AdminUser("Alexandros","Mikelis","Mika","admin2@dataverse.gr","newPassword123")
        valid_user = user
        
        output = valid_user.UserRegister()
        assert output=="\nYou are now registered\n"
        
    def test_UserPath1(self):
        """ UserPath1 : 
                Login -> Change Password -> Logout
            Note:
                Available for exery User
        """
        user = Users.AdminUser("Alexandros","Mikelis","Mika","admin2@dataverse.gr","newPassword123")
        valid_user = user
        starttime = time.time()
        
        output = valid_user.LogIn()
        assert output=="\nYou logged in Successfully\n"
        
        valid_user.ResetPassword(newPassword)
        valid_user.password = newPassword
        
        output = DatabaseSearch(user)
        assert output == 1
        
        output = valid_user.Logout(starttime)
        assert output == "You logged out"
    
    def test_UserPath2(self):
        """ UserPath2 : 
                Login -> Delete -> Logout
            Note:
                Available for exery User
        """
        user = Users.AdminUser("Alexandros","Mikelis","Mika","admin2@dataverse.gr","newPassword123")
        valid_user = user
        starttime = time.time()
        
        output = valid_user.LogIn()
        assert output=="\nYou logged in Successfully\n"
        
        valid_user.Delete()
        output =  DatabaseSearch(user)
        assert output == 0
        
        output = valid_user.Logout(starttime)
        assert output == "You logged out"
        
    def test_UserPath3(self):
        """ UserPath3 : 
                  Register
            Note:
                Available for exery User
        """
        user = Users.AdminUser("Alexandros","Mikelis","Mika","admin2@dataverse.gr","newPassword123")
        valid_user = user
        
        output = valid_user.UserRegister()
        assert output=="\nYou are now registered\n"
        
        
        