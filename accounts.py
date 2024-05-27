class Account_Balance:
     def __init__ (self):
        self.account_balance = 0
        print(self.account_balance)
        
     def deposit(self,deposit_amount):
         self.account_balance += deposit_amount
         return self.account_balance
     
     def minimum_balance(self):
         if(self.account_balance <= 499):
             print('Inssuficient account balance. Balance has to be either 500 KEshs. or more.')
         
         
         
     

class Account(Account_Balance):
    def __init__ (self):
       super().__init__()
       self.accounts_list = []
        
    def add_account_owner(self,account_user_name,account_pin):
        account_number = len(self.accounts_list)+1
        new_account_owner = {"account_user_name":account_user_name, "account_pin":account_pin, "account_number":account_number ,'Account_Balance':self.account_balance}
        self.accounts_list.append(new_account_owner)
        return self.accounts_list
        
    def display_details(self, input_account_pin):
        for user in self.accounts_list:
            if user['account_pin'] == input_account_pin:
             print(f'User Name:{user["account_user_name"]}\nAcount Number:{user["account_number"]}\nAccount Pin:{user["account_pin"]}\n {self.account_balance}')
        
    def change_account_owner(self, new_user_name, new_account_pin,old_account_number):
        for user in self.accounts_list:
            if old_account_number == user['account_number']:
                user['account_user_name'] = new_user_name
                user['account_pin'] = new_account_pin
                print(user)
                
    def transfer_funds(self,to_id,from_id, sent_amount):
        for user in self.accounts_list:
            if to_id == user['account_number'] and from_id == user['account_number']:
                if to_id == user['account_number']:
                    self.account_balance+= sent_amount
                    print(f'You have received {sent_amount} KEshs. from')
                    
                elif from_id == user['account_number']:
                    self.account_balance-= sent_amount

                
                
    def display_all(self):
        print(self.accounts_list)
                
                


new_user = Account()
new_user.deposit(400)
new_user.add_account_owner("Miki","234osk3")
new_user.display_details("234osk3")
new_user.minimum_balance()
new_user.change_account_owner("Canary","30ids",1)
new_user.add_account_owner("Miki","234osk3")
new_user.display_all()
new_user.transfer_funds(1,2,200)
new_user.deposit(600)





        
        
        
        