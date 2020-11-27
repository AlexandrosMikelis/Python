import UserSystemv4 as Users
import getpass
email = ""
password = ""
name=""
surname= ""
nickname=""
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
        user = Users.Staff(name,surname,nickname,email,password)
        user.LogIn()
        loginchoice = 0
        while(loginchoice != 3 and user.logpathcheck==1):
            user.Characteristics()
            user.ShowUsers()
            print("==========================")
            print("Press 1 -> Delete Account")
            print("Press 2 -> Change Password")
            print("Press 3 -> Logout")
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
            else:
                user.Logout()
                break
    else:
        break
