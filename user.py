from bankAccount import BankAccount


class User:
  def __init__(self, name, email):
    self.name = name
    self.email = email
    self.account = BankAccount(2, 0)

  def make_deposit(self, amount):
    try:
      self.account.deposit(amount)
    except ValueError as error:
      print(error)
    return self

  def make_withdrawl(self, amount):
    try:
      self.account.withdraw(amount)
    except ValueError as error:
      print(error)
    return self

  def display_balance(self):
    print(f'User: {self.name}, Balance: ${self.account.balance}')
    return self

  def transfer_money(self, other_user, amount):
    self.make_withdrawl(amount)
    other_user.make_deposit(amount)
    return self

justin = User('Justin', 'justin@email.com')
justin.make_deposit(200).make_deposit(400).make_deposit(100).make_withdrawl(300).display_balance()

lili = User('Lili', 'lili@email.com')
lili.make_deposit(500).make_deposit(200).make_withdrawl(200).make_withdrawl(200).display_balance()

other = User('Other', 'other@email.com')
other.make_deposit(500).make_withdrawl(200).make_withdrawl(200).make_withdrawl(200).display_balance()

justin.transfer_money(lili, 100)
justin.display_balance()
lili.display_balance()
