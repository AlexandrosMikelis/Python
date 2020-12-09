# -*- coding: utf-8 -*-
"""
Created on Mon Dec  7 16:20:04 2020

@author: Alex
"""

def DatabaseSearch(User):
    UserDB = open("UserDB.txt" , "r+")
    for Userss in UserDB :
        info = Userss.split(" ")
        if (info[0] == User.email and info[1] == User.password and 
            info[2] == User.name and info[3] == User.surname and 
            info[4] == User.nickname ):
            return 1
    return 0