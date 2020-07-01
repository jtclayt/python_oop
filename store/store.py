import unittest
from product import Product


class Store:
  def __init__(self, name):
    if (name != ''):
      self.name = name
      self.products = {}
    else:
      raise ValueError('Need to provide a name')

  def addProduct(self, newProduct):
    if isinstance(newProduct, Product):
      self.products[newProduct.id] = newProduct
    else:
      raise TypeError('Argument must be of type Product')
    return self

  def sellProduct(self, id):
    self.products.pop(id)
    return self

  def inflation(self, percentIncrease):
    for product in self.products.values():
      product.updatePrice(percentIncrease)
    return self

  def setClearance(self, category, percentDiscount):
    for product in self.products.values():
      if (product.category == category):
        product.updatePrice(percentDiscount, False)
    return self

  def printInventory(self):
    for product in self.products.values():
      product.printInfo()


class TestStore(unittest.TestCase):
  def setUp(self):
    self.testStore = Store('Test Store')

  def testStoreCreated(self):
    store = Store('My Store')
    self.assertIsNotNone(store)
    self.assertEqual('My Store', store.name)

  def testNoStoreName(self):
    self.assertRaises(ValueError, Store, '')

  def testAddProduct(self):
    newProduct = Product('Banana', 1.5, 'fruit')
    self.testStore.addProduct(newProduct)
    self.assertEqual(1, len(self.testStore.products))
    self.assertEqual('Banana', self.testStore.products[newProduct.id].name)

  def testAddNotProduct(self):
    self.assertRaises(TypeError, self.testStore.addProduct, 'Not a product')

  def testSellProduct(self):
    newProduct = Product('Banana', 1.5, 'fruit')
    self.testStore.addProduct(newProduct)
    self.testStore.sellProduct(newProduct.id)
    self.assertEqual(0, len(self.testStore.products))

  def testInflation(self):
    prod1 = Product('Banana', 1.5, 'fruit')
    prod2 = Product('Celery', 1, 'vegetable')
    self.testStore.addProduct(prod1).addProduct(prod2).inflation(5)
    self.assertEqual(1.5*1.05, self.testStore.products[prod1.id].price)
    self.assertEqual(1.05, self.testStore.products[prod2.id].price)

  def testClearance(self):
    prod1 = Product('Banana', 1.5, 'fruit')
    prod2 = Product('Celery', 1, 'vegetable')
    self.testStore.addProduct(prod1).addProduct(prod2).setClearance('fruit', 10)
    self.assertEqual(1.5*0.9, self.testStore.products[prod1.id].price)
    self.assertEqual(1, self.testStore.products[prod2.id].price)

if (__name__ == '__main__'):
  unittest.main()