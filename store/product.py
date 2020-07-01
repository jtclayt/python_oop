import unittest


class Product:
  nextId = 1

  def __init__(self, name, price, category):
    if (name == '' or category == ''):
      raise ValueError('Need to provide name and category')
    elif (price <= 0):
      raise ValueError('Price must be a positive number')
    else:
      self.id = f'prd-{Product.nextId}'
      Product.nextId += 1
      self.name = name
      self.price = price
      self.category = category

  def updatePrice(self, percentChange, isIncreased=True):
    percentChange /= 100
    if isIncreased:
      self.price *= 1 + percentChange
    else:
      self.price *= 1- percentChange

  def printInfo(self):
    print(f'{self.name} - ${round(self.price, 2)} - {self.category}')


class TestProduct(unittest.TestCase):
  def setUp(self):
    self.testProduct = Product('Banana', 1.5, 'fruit')

  def testCreateProduct(self):
    product = Product('thing', 7, 'object')
    self.assertIsNotNone(product)
    self.assertEqual('thing', product.name)
    self.assertEqual(7, product.price)
    self.assertEqual('object', product.category)

  def testBadProducts(self):
    self.assertRaises(ValueError, Product, '', 1, 'stuff')
    self.assertRaises(ValueError, Product, 'stuff', -2, 'stuff')
    self.assertRaises(ValueError, Product, 'stuff', 1, '')

  def testChangePrice(self):
    self.testProduct.updatePrice(5)
    newPrice = 1.5 * 1.05
    self.assertEqual(newPrice, self.testProduct.price)
    self.testProduct.updatePrice(10, False)
    newPrice *= 0.9
    self.assertEqual(newPrice, self.testProduct.price)

  def testUniqueId(self):
    self.assertEqual('prd-5', self.testProduct.id)
    self.product2 = Product('Apple', 1, 'fruit')
    self.assertEqual('prd-6', self.product2.id)

if (__name__ == '__main__'):
  unittest.main()
