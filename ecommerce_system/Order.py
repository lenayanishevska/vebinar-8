from ecommerce_system import User, Warehouse


class Order:
    def __init__(self, user: User, warehouse: Warehouse):
        self.user = user
        self.warehouse = warehouse

    def place_order(self):
        for product, quantity in self.user.shopping_cart.items.items():
            if product in self.warehouse.storage and self.warehouse.storage[product] >= quantity:
                self.warehouse.storage[product] -= quantity
            else:
                print(f"Insufficient stock for {product.name}")

        self.user.shopping_cart.items = {}

