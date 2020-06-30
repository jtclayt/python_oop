class User:
  def __init__(self, name, email):
    self.name = name
    self.email = email
    self.account_balance = 0

  def make_deposit(self, amount):
    if (amount <= 0):
      print('Amount can not be less than 0.')
    else:
      self.account_balance += amount

  def make_withdrawl(self, amount):
    if (amount <= 0):
      print('Amount can not be less than 0.')
    elif (amount > self.account_balance):
      print('Insufficient funds for withdrawl.')
    else:
      self.account_balance -= amount

  def display_balance(self):
    print(f'User: {self.name}, Balance: ${self.account_balance}')

  def transfer_money(self, other_user, amount):
    self.make_withdrawl(amount)
    other_user.make_deposit(amount)

justin = User('Justin', 'justin@email.com')
justin.make_deposit(200)
justin.make_deposit(400)
justin.make_deposit(100)
justin.make_withdrawl(300)
justin.display_balance()
lili = User('Lili', 'lili@email.com')
lili.make_deposit(500)
lili.make_deposit(200)
lili.make_withdrawl(200)
lili.make_withdrawl(200)
lili.display_balance()
other = User('Other', 'other@email.com')
other.make_deposit(500)
other.make_withdrawl(200)
other.make_withdrawl(200)
other.make_withdrawl(200)
other.display_balance()
justin.transfer_money(lili, 100)
justin.display_balance()
lili.display_balance()