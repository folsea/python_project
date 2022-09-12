class Protected: #  protected 
    def __init__(self):
        self.protectedVar = 0

obj = Protected() # use of protected
obj._protectedVar = 34
print(obj._protectedVar) 

class Protected: # private 
    def __init__ (self):
        self.__privateVar = 12

    def getPrivate(self):
        print(self.__privateVar)

    def setPrivate(self, private):
        self.__privateVar =  private

obj = Protected() #use of provate and protected coding 
obj.getPrivate()
obj.setPrivate(23)
obj.getPrivate()
        
