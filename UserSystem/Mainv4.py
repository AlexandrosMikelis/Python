import UserSystemv5 as Users
import getpass    
email = ""
password = ""
name=""
surname= ""
nickname=""
admin = 0
staff = 0
while(1):
    print("==========================")
    print("Press 0 -> Exit ")
    print("Press 1 -> Register ")
    print("Press 2 -> Login ")
    print("==========================")
    choice = int(input("Choice : "))
    if(choice==1):
        email = input("Email : ")
        email = email.replace(" ","")
        print("***At least one Capital one lower and one number***")
        password = input("New password : ")
        password = password.replace(" ","")
        repass = input("Repeat new password : ")
        repass = repass.replace(" ","")
        name = input("Name : ")
        surname = input("Surname : ")
        nickname = input("Type your nickname : ")
        if(repass == password ):
            user = Users.SimpleUser(name,surname,nickname,email,password)
            user.UserRegister()
    elif(choice == 2):
        email = input("Email : ")
        email = email.replace(" " ,"")
        password = getpass.getpass(prompt='Password: ', stream=None)
        password = password.replace(" ","")
        UserDB = open("UserDB.txt" , "r")
        for Userss in UserDB :
            info = Userss.split(" ")
            if email == info[0] and password == info[1] :
                name = info[2]
                surname = info[3]
                nickname = info[4][:-1]
        if email[-12:-3]=="dataverse" and email[0:5] == "admin":
            user = Users.AdminUser(name,surname,nickname,email,password)
            admin = 1
        elif email[-12:-3]=="dataverse":
            user = Users.StaffUser(name,surname,nickname,email,password)
            staff = 1
        else:
            user = Users.SimpleUser(name,surname,nickname,email,password)
        user.LogIn()
        loginchoice = 0
        while(loginchoice != 3 and user.logpathcheck==1):
            user.Characteristics()
            print("==========================")
            print("Press 1 -> Delete Account")
            print("Press 2 -> Change Password")
            print("Press 3 -> Logout")
            
            if(admin == 1 or staff ==1):
                print("Press 4 -> Show Users")
                print("Press 5 -> Warn Users")
                if(admin==0):
                    print("==========================") 
            else:
                print("==========================") 
                
            if(admin == 1 ):
                print("Press 6 -> Delete Users")
                print("Press 7 -> Ban Users")
                print("==========================") 
            loginchoice= int(input("Choice: "))
            if(loginchoice == 1):
                if(email!="" and password!=""):
                    user.Delete()
                    print("Your account is deleted")
                    break
                else:
                    print("You need to login first!")
            elif(loginchoice == 2):
                if(email!="" and password!=""):
                    new_password = input("Type new password : ")
                    renew_password = input("Type again new password : ")
                    if(new_password==renew_password):
                        user.ResetPassword(new_password)
                else:
                    print("You need to login first")
            elif (loginchoice == 3):
                user.Logout()
                break
            else:
                if ((admin ==1 or staff==1) and loginchoice == 4):
                    print("Showing Users...")
                    user.UsersDisplay()
                elif((admin ==1 or staff==1) and loginchoice == 5):
                    print("warning Users...")
                    Email = input("Type email of the user : ")
                    temp = input("Are you sure you want to warn {} [y/n]".format(Email))
                    if temp == "y":
                        user.Warn(Email)
                elif(admin ==1  and loginchoice == 6):
                    print("Deleting Users...")
                    Email = input("Type email of the user : ")
                    temp = input("Are you sure you want to delete {} [y/n]".format(Email))
                    if temp == "y":
                        for Userss in UserDB :
                            info = Userss.split(" ")
                            if Email == info[0]:
                                password == info[1] 
                                name = info[2]
                                surname = info[3]
                                nickname = info[4][:-1]
                                break
                        tempuser = Users.SimpleUser(name,surname,nickname,email,password)
                        tempuser.Delete()                       
                elif(admin ==1  and loginchoice == 7):
                    print("Banning Users...")
                    Email = input("Type email of the user : ")
                    temp = input("Are you sure you want to ban {} [y/n]".format(Email))
                    if temp == "y":
                        user.Ban(Email)
                else:
                    print("Invalid option")
                    
                
    else:
        break
