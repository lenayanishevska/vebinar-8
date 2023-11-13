from ecommerce_system import Product


class Warehouse:
    def __init__(self):
        self.storage = {}

    def add_product(self, product: Product, quantity):
        if product in self.storage:
            self.storage[product] += quantity
        else:
            self.storage[product] = quantity

    def view_stock(self):
        result = "In stock:\n"
        for product, quantity in self.storage.items():
            result += f"{product} : {quantity}\n"
        return result.strip()

