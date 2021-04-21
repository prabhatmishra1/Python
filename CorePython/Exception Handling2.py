#How to create exception class.
class InsufficientBalance(ZeroDivisionError):
  def __init__(self,arg):#constructor
      self.msg=arg
balance=5000
w=int(input("Enter amount to withdraw:"))
try:
  if w>balance:
        raise InsufficientBalance("Insufficient Balance in the account")
  balance=balance-w
except InsufficientBalance as i:
    print("Exception:",i.msg)
else:
    print("Withdraw ammount",w,"sucessufuly")
finally:
    print("Current Balance is:",balance)
 
