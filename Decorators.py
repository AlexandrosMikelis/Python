import time
import datetime

def newChars(func):
    def inner(*args,**kwargs):
        print("Username : " + args[0].nickname+ "\nName : " + args[0].name 
              + "\nSurname : " + args[0].surname + "\nEmail : " + args[0].email+ "\n")
        func(*args,**kwargs)
    return inner

def timeit(func):
    def timed(*args, **kw):
        ts = args[1]
        te = time.time()
        print("Your Session Lasted {} secs".format(te-ts))
        newDB = []
        UserDB = open("UserDB.txt" , "r+")
        for Userss in UserDB :
            info = Userss.split(" ")
            if(info[0]!=args[0].email):
                newDB.append(Userss)
            else:
                newDB.append(args[0].email + " " + args[0].password + " " + args[0].name 
                             + " " + args[0].surname + " "+ args[0].nickname + " " + 
                             str(datetime.datetime.now()) +'\n')
        UserDB.seek(0)
        for i in newDB:
            UserDB.write(i)
        UserDB.close()
        return func(*args, **kw)
    return timed
def UserShowcase(func):
    def UserShow(*args, **kw):
        UserDB = open("UserDB.txt" , "r")
        for Users in UserDB :
            print(Users)
    return UserShow