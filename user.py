class User:
  def __init__(self, name, email):
    if (name == '' or email == ''):
      return None
    self.name = name
    self.email = email
    self.account_balance = 0

  def make_deposit(self, amount):
    if (amount > 0):
      self.account_balance += amount

  def make_withdrawl(self, amount):
    if (amount > 0):
      self.account_balance -= amount

  def display_balance(self):
    print(f'User: {self.name}, Balance: ${self.account_balance}')

  def transfer_money(self, other_user, amount):
    self.make_withdrawl(amount)
    other_user.make_deposit(amount)

justin = User('Justin', 'lili@email.com')
justin.make_deposit(200)
justin.display_balance()
lili = User('Lili', 'lili@email.com')
justin.transfer_money(lili, 100)
justin.display_balance()
lili.display_balance()