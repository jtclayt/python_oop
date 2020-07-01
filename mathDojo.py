import unittest
import random

class MathDojo:
  def __init__(self):
    self.result = 0

  def add(self, num, *nums):
    sum = num
    for val in nums:
      sum += val
    self.result += sum
    return self

  def subtract(self, num, *nums):
    sum = num
    for val in nums:
      sum += val
    self.result -= sum
    return self


class TestMathDojo(unittest.TestCase):
  def setUp(self):
    self.md = MathDojo()

  def testAdd(self):
    self.md.add(4)
    self.assertEqual(self.md.result, 4)

  def testAddMultiple(self):
    self.md.add(4,3,5,1)
    self.assertEqual(self.md.result, 13)

  def testSubtract(self):
    self.md.subtract(2)
    self.assertEqual(self.md.result, -2)

  def testSubtractMultiple(self):
    self.md.subtract(2,10)
    self.assertEqual(self.md.result, -12)

  def testChaining(self):
    self.md.add(1,3,5,7).subtract(2,4,6)
    self.assertEqual(self.md.result, 4)

  def testRandom(self):
    answer = 0
    for _ in range(20):
      num1 = random.randint(0,100)
      num2 = random.randint(0,100)
      num3 = random.randint(0,100)
      isAdding = random.choice([True, False])
      if (isAdding):
        answer += (num1 + num2 + num3)
        self.md.add(num1, num2, num3)
      else:
        answer -= (num1 + num2 + num3)
        self.md.subtract(num1, num2, num3)
      self.assertEqual(self.md.result, answer)

if (__name__ == '__main__'):
  unittest.main()
