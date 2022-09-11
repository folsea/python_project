class User: #parent classs 
    name = 'No Name Provided'
    email = ' '
    password ='1234abcd'
    account_number = 0


class Subscription(User): #this verifies if the subscription is paid and cost 
    memebership_cost= 5
    member_level='paid'

class Member(User):#contact information 
     mailing_adress =''
     mailing_list = True 
    
