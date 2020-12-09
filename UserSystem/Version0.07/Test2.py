import TestsFunctions as TestF

N_USERS = 10
LABEL = "Simple"   # <===== Admin = Check N_USERS admins Staff == ... Simple=...


class TestClass:
    
    
    def User_Validate_Credantials0(self):
        """ UserPath0 : 
                  Register
            Note:
                Available for exery User
        """
        
        user = TestF.SpawnRandomUsers(N_USERS,LABEL,False)
        for i in range(len(user)):
            valid_user = user[i]
        
            output = valid_user.UserRegister()
            assert output=="""\n!!!Your password need to have at least one alphabetic 
                      , digit , lower and a capital character!!!\n"""
        