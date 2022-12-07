class Product:
    def __init__(self, name, price):
        self.name = name
        self.price = price
        self.quantity = 1
    
    def get_price(self):
        print(f"The price for 1x of {self.name} is ${self.price:.2f}.")
    
class Cart:
    def __init__(self):
        self.cart = []
    
    def add_product(self, product, quantity):
        self.cart.append(product)
        product.quantity = quantity

    def remove_product(self, product, quantity):
        product.quantity -= quantity
        if product.quantity == 0:
            self.cart.remove(product)

    def get_total(self):
        total = 0
        for product in self.cart:
            total += product.price * product.quantity
        print(f"${total:.2f}")

    def display_cart(self):
        print("--Cart--")
        for pdt in self.cart:
            print(f"{pdt.name}: {pdt.quantity}")

# create the cart and product objects
trolley = Cart()
product_001 = Product("Apple", 0.60)
product_002 = Product("Banana", 1.40)

# add the items to the cart
trolley.add_product(product_001, 5)
trolley.add_product(product_002, 1)

# display the items in the cart
trolley.display_cart()

# remove an item from the cart
trolley.remove_product(product_002, 1)

# get the total cost of all items in the cart
trolley.display_cart()
trolley.get_total()