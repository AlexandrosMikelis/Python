import UserFormVersion2 as Users

email = ""
password = ""
name=""
surname= ""
nickname=""
while(1):
    print("Press 0 -> Exit ")
    print("Press 1 -> Register ")
    print("Press 2 -> Login ")
    choice = int(input("Choice : "))
    if(choice==1):
        email = input("Email : ")
        password = input("New password : ")
        repass = input("Repeat new password : ")
        name = input("Name : ")
        surname = input("Surname : ")
        nickname = input("Type your nickname : ")
        if(repass == password ):
            user = Users.SimpleUser(name,surname,nickname,email,password,0,0,0)
            user.UserRegister()
    elif(choice == 2):
        email = input("Email : ")
        password = input("Password : ")
        user = Users.SimpleUser(name,surname,nickname,email,password,0,0,0)
        user.LogIn()
        loginchoice = 0
        while(loginchoice != 3):
            print("Press 1 -> Delete Account")
            print("Press 2 -> Change Password")
            print("Press 3 -> Logout")
            loginchoice= int(input("Choice: "))
            if(loginchoice == 1):
                if(email!="" and password!=""):
                    user = Users.SimpleUser(name,surname,nickname,email,password,0,0,0)
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
                break
    else:
        break
