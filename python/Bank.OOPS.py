class User:
    
    def __init__(self,pin):
        self.pin = pin

    def login(self,entered_pin):
        if entered_pin == self.pin:
            print("Logged In")
        else:
             print("Incorrect Password")

    def logout(self):
        print("Logged Out")



u = User(123);
u.login(124)
u.logout()

