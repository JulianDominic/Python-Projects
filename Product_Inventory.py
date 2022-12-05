"""
Product Inventory Project - Create an application which manages an inventory of products. Create a product class which has a price, id, and quantity on hand. Then create an inventory class which keeps track of various products and can sum up the inventory value.
"""
class Product:
    def __init__(self, price, id, quantity):
        self.price = price
        self.id = id
        self.quantity = quantity
        

class Inventory:
    def __init__(self):
        self.products = []
    
    def add_product(self, product):
        self.products.append(product)
    
    def update_product_quantity(self, product, new_quantity):
        product.quantity = new_quantity
    
    def update_product_price(self, product, new_price):
        product.price = new_price
    
    def search_product(self, product_id):
        for product in self.products:
            if product.id == product_id:
                return product
        return None
    
    def calculate_inventory_value(self):
        total_value = 0
        for product in self.products:
            total_value += product.quantity * product.price
        return total_value



def main():
    inv = Inventory()
    apple = Product(0.5, "01", 50)

    inv.add_product(apple)
    print(inv.calculate_inventory_value())

    inv.update_product_quantity(apple, 100)
    print(inv.calculate_inventory_value())

    inv.update_product_price(apple, 65)
    print(inv.calculate_inventory_value())

    print(inv.search_product("01"))

if __name__== "__main__":
    main()