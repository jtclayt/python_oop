from store import Store
from product import Product


def main():
  coffeeStore = Store('PF Roasting')
  lightCoffee = Product('Light Coffee', 2, 'bev')
  darkCoffee = Product('Dark Coffee', 1.75, 'bev')
  scone = Product('Scone', 3, 'food')
  darkCoffee.printInfo()
  coffeeStore.addProduct(lightCoffee).addProduct(darkCoffee).addProduct(scone)
  coffeeStore.printInventory()
  coffeeStore.inflation(5)
  coffeeStore.setClearance('bev', 25)
  coffeeStore.printInventory()
  coffeeStore.sellProduct(lightCoffee.id)
  coffeeStore.printInventory()


if __name__ == '__main__':
  main()