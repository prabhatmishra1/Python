'''Define class account with static variable rate_of_interest instance variables balance and account number. make function to set value in instance
object of account.show balance,show rate_of_inerest,withdraw and deposit.'''
class account:
    rtf=10
    def statement(self,accno):
        self.accno=accno
        self.balance=50000
        print("Account Details:\n\nAccno:%d\nbalance:%d\nRate_of_interest:%d"%(self.accno,self.balance,account.rtf))
        w=int(input("Enter the amount to withdraw:"))
        self.balance=self.balance-w
        print("%d has been withdraw from your account"%w)
        print("Account Details:\n\nAccno:%d\nbalance:%d\nRate_of_interest:%d"%(self.accno,self.balance,account.rtf))
        w=int(input("Enter the amount to Deposit:"))
        self.balance=self.balance+w
        print("%d has been Deposit in your account"%w)
        print("Account Details:\n\nAccno:%d\nbalance:%d\nRate_of_interest:%d"%(self.accno,self.balance,account.rtf))
        
obj1=account()
obj1.statement(4198181828713)


        
    
