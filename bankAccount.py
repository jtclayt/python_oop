import unittest


class BankAccount:
  def __init__(self, int_rate, balance=0):
    if (int_rate < 0):
      raise ValueError('Can not have negative interest rate')
    if (balance < 0):
      raise ValueError('Can not have negative balance')
    self.int_rate = int_rate / 100
    self.balance = balance

  def deposit(self, amount):
    if (amount <= 0):
      raise ValueError('Amount must be positive')
    else:
      self.balance += amount
    return self

  def withdraw(self, amount):
    if (amount <= 0):
      raise ValueError('Amount must be positive')
    elif (amount > self.balance):
      raise ValueError('Insufficient funds')
    else:
      self.balance -= amount
    return self

  def display_account_info(self):
    print(f'\nBalance: ${round(self.balance, 2)}')

  def yield_interest(self):
    self.balance *= 1 + self.int_rate
    return self


class TestBankAccount(unittest.TestCase):
  def setUp(self):
    self.account1 = BankAccount(1, 200)
    self.account2 = BankAccount(3, 2000)

  def testCreateAccount(self):
    testAccount = BankAccount(5, 100)
    self.assertEqual(0.05, testAccount.int_rate)
    self.assertEqual(100, testAccount.balance)

  def testBadInterest(self):
    self.assertRaises(ValueError, BankAccount, -2, 100)

  def testBadBalance(self):
    self.assertRaises(ValueError, BankAccount, 2, -100)

  def testWithdrawal(self):
    self.account1.withdraw(100)
    self.assertEqual(100, self.account1.balance)

  def testOverdraw(self):
    self.assertRaises(ValueError, self.account1.withdraw, 500)

  def testNegWithdrawal(self):
    self.assertRaises(ValueError, self.account1.withdraw, -100)

  def testDeposit(self):
    self.account1.deposit(100)
    self.assertEqual(300, self.account1.balance)

  def testNegDeposit(self):
    self.assertRaises(ValueError, self.account1.deposit, -100)

  def testYieldInterest(self):
    self.account1.yield_interest()
    self.assertEqual(200*1.01, self.account1.balance)

  def testUse(self):
    self.account1.deposit(100).deposit(100).deposit(100).withdraw(400)
    self.account1.display_account_info()
    self.assertEqual(100, self.account1.balance)
    self.account2.deposit(100).deposit(100).withdraw(400).withdraw(400)
    self.account2.withdraw(400).yield_interest().display_account_info()
    self.assertEqual(1000*1.03, self.account2.balance)

if __name__ == '__main__':
  unittest.main()
