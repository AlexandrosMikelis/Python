# -*- coding: utf-8 -*-
"""
Created on Mon Dec  7 11:34:58 2020

@author: Alex
"""
import UserSection as Users
import time 
import random
import TestsFunctions as TestF

starttime = 0
validuser = 0
Email = "iamalekos@hotmail.com"
newPassword = "newPassword123"
N_USERS = 10
LABEL = "Simple"   # <===== Admin = Check N_USERS admins Staff == ... Simple=...

class TestClass:
    
    
    def test_UserPath0(self):
        """ UserPath0 : 
                  Register
            Note:
                Available for exery User
        """
        
        user = TestF.SpawnRandomUsers(N_USERS,LABEL,True)
        for i in range(len(user)):
            valid_user = user[i]
        
            output = valid_user.UserRegister()
            assert output=="\nYou are now registered\n"
     
        
     
    def test_UserPath1(self):
        """ UserPath1 : 
                Login -> Change Password -> Logout
            Note:
                Available for exery User
            otan o user ftiaxnete globaly kai kanei logout xanete h plhroforia 
            tou an einai logged in h oxi opote prepei na ksanaftiaxtei
        """
        user = TestF.SpawnRandomUsers(N_USERS,LABEL,True)
        
        for i in range(len(user)):
            
            valid_user = user[i]
            starttime = time.time()
            
            valid_user.GetValidation()
            
            output = valid_user.LogIn()
            assert output=="\nYou logged in Successfully\n"
            
            valid_user.ResetPassword(newPassword)
            valid_user.password = newPassword
            
            output = TestF.DatabaseSearch(user[i])
            assert output == 1
            
            output = valid_user.Logout(starttime)
            assert output == "You logged out"
            
            
    def test_UserPath2(self):
        """ UserPath3 : 
                  Admin Login -> Characteristics -> UsersDisplay -> Warn -> Ban
                  ->Logout
            Note:
                Available for exery User
        """
        user = TestF.SpawnRandomUsers(N_USERS,LABEL,True)
        
        for i in range(len(user)):
            valid_user = user[i]
            
            valid_user.GetValidation()
            
            output = valid_user.LogIn()
            assert output=="\nYou logged in Successfully\n"
            
            output = valid_user.Characteristics()
            assert output == "|You are {} User    |".format(LABEL)
            
            try:
                output = valid_user.UsersDisplay()
                assert output == "Complete" 
                
                output = valid_user.Warn(Email)
                assert output == "Sending Warning to {}".format(Email) 
                
                try:
                    output = valid_user.Ban(Email)
                    assert output == "Banning {}".format(Email) 
                except:
                    pass
            except:
                pass
            
            
            
    def test_UserPath3(self):
        """ UserPath2 : 
                Login -> Delete -> Logout
            Note:
                Available for exery User
        """
        user = TestF.SpawnRandomUsers(N_USERS,LABEL,True)
        
        for i in range(len(user)):
            
            valid_user = user[i]
            starttime = time.time()
            
            valid_user.GetValidation()
            
            output = valid_user.LogIn()
            assert output=="\nYou logged in Successfully\n"
            
            valid_user.Delete()
            output =  TestF.DatabaseSearch(user[i])
            assert output == 0
            
            output = valid_user.Logout(starttime)
            assert output == "You logged out"
    
            
        
        