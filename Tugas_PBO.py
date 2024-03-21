#Pemrograman fungsional
#Mendefinisikan list prices
prices = [10, 20, 30, 40]

#Mendefinisikan fungsi untuk menghitung total harga
def total(prices):
  return sum(prices)

#Mencetak hasil dari fungsi total() dengan parameter prices
print(total(prices))


#OOP (Object-Oriented Programming) 
#Mendefinisikan sebuah class Item untuk merepresentasikan sebuah item
class Item:
  def __init__(self, name, price):
    self.name = name
    self.price = price

#Mendefinisikan sebuah class ShoppingCart untuk merepresentasikan sebuah shopping cart
class ShoppingCart:
  def __init__(self):
    self.items = []

  def add_item(self, item):
    self.items.append(item)

  def total(self):
    #Menghitung total harga dari seluruh item di dalam shopping cart
    return sum(item.price for item in self.items)

#Membuat sebuah instance dari class ShoppingCart
cart = ShoppingCart()

#Menambahkan beberapa item ke dalam shopping cart
cart.add_item(Item("Buku", 10))
cart.add_item(Item("Pulpen", 5))
cart.add_item(Item("Kertas", 20))

#Mencetak total harga dari seluruh item di dalam shopping cart
print(cart.total())
