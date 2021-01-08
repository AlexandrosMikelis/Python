import UserSystemv6 as Users
import random

def DatabaseSearch(User):
    
    UserDB = open("UserDB.txt" , "r+")
    for Userss in UserDB :
        
        info = Userss.split(" ")
        
        if ((info[0] == User.email and 
             info[1] == User.password and 
             info[2] == User.name and 
             info[3] == User.surname and 
             info[4][:-1] == User.nickname)
            or 
            (info[0] == User.email and 
             info[1] == User.password and 
             info[2] == User.name and 
             info[3] == User.surname and 
             info[4] == User.nickname )):
            return 1
    return 0


def SpawnRandomUsers(length,label,validation):
    randomUsers=[]
    if validation == True :
        password = "newPassword123"
    else:
        password = "newpassword123"
    if label == "Admin":
        for i in range(length):
            randomUsers.append(Users.AdminUser("Type" + str(i) , 
                                               "Name" + str(i) ,
                                               "TypeName" + str(i) ,
                                               "Admin"+ str(i) + "@dataverse.gr",
                                               password))
    elif label =="Staff":
        for i in range(length):
            randomUsers.append(Users.StaffUser("Type" + str(i) , 
                                               "Name" + str(i) ,
                                               "TypeName" + str(i) ,
                                               "Staff"+ str(i) + "@dataverse.gr",
                                               password))
    elif label == "Simple":
        for i in range(length):
            randomUsers.append(Users.SimpleUser("Type" + str(i) , 
                                               "Name" + str(i) ,
                                               "TypeName" + str(i) ,
                                               "Simple"+ str(i) + "@gmail.gr",
                                               password))
    elif label == "Random":
        pass
    else:
        return 0
    return randomUsers

