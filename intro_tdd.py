import unittest


def reverseList(arr):
  mid = len(arr) // 2
  for i in range(mid):
    end = len(arr) - 1 - i
    arr[i], arr[end] = arr[end], arr[i]
  return arr

def isPalindrome(word):
  mid = len(word) // 2
  for i in range(mid):
    end = len(word) - 1 - i
    if(word[i] != word[end]):
      return False
  return True

def coins(cents):
  coinVals = [25,10,5,1]
  coinList = [0,0,0,0]
  for i in range(len(coinVals)):
    val = coinVals[i]
    while (cents / val >= 1):
      coinList[i] += 1
      cents -= val
  return coinList

def factorial(num):
  if (num == 0):
    return 1
  return num * factorial(num-1)

def fib(index):
  if (index == 0):
    return 0
  elif(index == 1 or index == 2):
    return 1
  return fib(index - 1) + fib(index - 2)


class TestFunctions(unittest.TestCase):
  def testReverseList(self):
    self.assertEqual(reverseList([1,3,5]), [5,3,1])
    self.assertEqual(reverseList([1,2,7,3]), [3,7,2,1])
    self.assertEqual(reverseList([1]), [1])
    self.assertEqual(reverseList([]), [])

  def testIsPalindrome(self):
    self.assertTrue(isPalindrome('racecar'))
    self.assertTrue(isPalindrome('abccba'))
    self.assertTrue(isPalindrome('aa'))
    self.assertTrue(isPalindrome('a'))
    self.assertFalse(isPalindrome('rabcr'))
    self.assertFalse(isPalindrome('word'))
    self.assertFalse(isPalindrome('hlelo'))
    self.assertFalse(isPalindrome('mmh'))

  def testCoins(self):
    self.assertEqual(coins(87), [3,1,0,2])
    self.assertEqual(coins(1), [0,0,0,1])
    self.assertEqual(coins(0), [0,0,0,0])
    self.assertEqual(coins(99), [3,2,0,4])
    self.assertEqual(coins(10), [0,1,0,0])
    self.assertEqual(coins(83), [3,0,1,3])

  def testFactorial(self):
    self.assertEqual(factorial(5), 120)
    self.assertEqual(factorial(1), 1)
    self.assertEqual(factorial(0), 1)
    self.assertEqual(factorial(3), 6)

  def testFibonacci(self):
    self.assertEqual(fib(0), 0)
    self.assertEqual(fib(1), 1)
    self.assertEqual(fib(2), 1)
    self.assertEqual(fib(5), 5)
    self.assertEqual(fib(8), 21)


if (__name__ == '__main__'):
  unittest.main()