# Parent Class User
class User:
    name = "Mark"
    email = "mark@gmail.com"
    password = "123abcd"

    def getLoginInfo (self):
        entry_name = input("Enter you name: ")
        entry_email = input("Enter you email: ")
        entry_password = input("Enter you passwrod: ")
        if (entry_email == self.email and entry_password == self.password) :
            print("Welcome back, {}!".format(entry_name))
        else:
            print("The passworn or email is incorrect.")
        
#Child Class Employee
class Employee(User):
    base_pay = 11.00
    department = "General"
    pin_number = "3980"


class Manger(User):
    base_pay= 15.00
    department = "Managment"
    pin_number= "2356"
    
# THis is the same mathod in the parent class "User".
#The diffenece is that, instead of using entry_password, we're using entry_pin.

    def getLoginInfo(self):
        entry_name = input("Enter you name: ")
        entry_email = input("Enter your email: ")
        entry_pin = input("Enter your pin: ")
        if (entry_email == self.email and entry_pin == self.pin_number):
            print("Welcome back, {}!".format(entry_name))
        else:
            print("The pin or email is incorrect")

#The following code invokes the methods inside each class for User and EMployee.
    
customer = User()
customer.getLoginInfo()
manager = Employee()
manager.getLoginInfo() 
                            
