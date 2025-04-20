class Product:
    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity

    def __str__(self):
        return f'Product: {self.name}, Price: {self.price}, Quantity: {self.quantity}'
    
class ShoppingCart:
    def __init__(self):
        self.cart = []

    def addtocart(self, product):
        self.cart.append(product)
    
    def view_cart(self):
        for i, product in enumerate(self.cart):
            print(f'{i + 1}: {product}')

    def remove(self, index):
        if 0 <= index < len(self.cart):
            self.cart.pop(index)
            print('Item removed!')
        else:
            print('Item does not exist')
