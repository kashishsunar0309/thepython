class account:
  def __init__(self,bal,acc):
    self.balance = bal
    self.account_number = acc
  def credit(self,amount):
    self.balance += amount
    print("Your balance has been credited Rs",amount)
    print("Total balance is RS",self.get_balance())
  def debit(self,amount):
    self.balance -= amount
    print("Your balance has been debited Rs",amount)
    print("Total balance is Rs",self.get_balance())
  def get_balance(self):
    return self.balance

acc1= account(50000,2323)
print("Total Balance:",acc1.balance)#for account balance
print("Account Number:",acc1.account_number)#for account number
acc1.credit(5000)#for credit Bonus
acc1.debit(45000)#for debit Loan of Car