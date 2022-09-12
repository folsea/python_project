from abc import ABC, abstractmethod
class car(ABC):
    def paySlip (self, amount):
        print("Your purchase amount: ",amount)
#this function will cause a bypass in an argument,
        @abstractmethod
        def payment(self, amount):
            pass

class DebitCardPayment(car):
#how to use payment function from payslip
    def payment(self, amount):
        print('Your purchase amount of {} exceeded your $100 limit '.format(amount) )

obj = DebitCardPayment()
obj.paySlip("400")
obj.payment("$400") 
