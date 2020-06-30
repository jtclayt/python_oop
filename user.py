from bankAccount import BankAccount


class User:
  def __init__(self, name, email):
    self.name = name
    self.email = email
    self.accounts = [BankAccount(2, 0)]

  def make_deposit(self, amount, acct_num=0):
    try:
      self.accounts[acct_num].deposit(amount)
    except ValueError as error:
      print(error)
    except IndexError:
      print('No account found with that number')
    return self

  def make_withdrawal(self, amount, acct_num=0):
    try:
      self.accounts[acct_num].withdraw(amount)
    except ValueError as error:
      print(error)
    except IndexError:
      print('No account found with that number')
    return self

  def add_account(self, int_rate=2, balance=0):
    try:
      self.accounts.append(BankAccount(int_rate, balance))
    except ValueError as error:
      print(error)
    return self

  def display_balance(self, acct_num=0):
    try:
      print(
        f'User: {self.name}, '
        f'Account: {acct_num}, '
        f'Balance: ${self.accounts[acct_num].balance}'
      )
    except IndexError:
      print('No account found with that number')
    return self

  def transfer_money(self, other_user, amount):
    self.make_withdrawal(amount)
    other_user.make_deposit(amount)
    return self

justin = User('Justin', 'justin@email.com')
justin.make_deposit(200).make_deposit(400).make_deposit(100).make_withdrawal(300).display_balance()

lili = User('Lili', 'lili@email.com')
lili.make_deposit(500).make_deposit(200).make_withdrawal(200).make_withdrawal(200).display_balance()

other = User('Other', 'other@email.com')
other.make_deposit(500).make_withdrawal(200).make_withdrawal(200).make_withdrawal(200).display_balance()

justin.transfer_money(lili, 100)
justin.display_balance()
lili.display_balance()

justin.add_account(5, 200)
justin.display_balance(1)
justin.display_balance(2)
justin.make_withdrawal(100, 2)
