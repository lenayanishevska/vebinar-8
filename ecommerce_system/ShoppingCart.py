from ecommerce_system import Product


class ShoppingCart:
    def __init__(self):
        self.items = {}

    def add_item(self, product: Product, quantity):
        if product in self.items:
            self.items[product] += quantity
        else:
            self.items[product] = quantity

