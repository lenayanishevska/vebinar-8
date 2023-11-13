from ShoppingCart import ShoppingCart


class User:
    def __init__(self, name, email):
        self.name = name
        self.email = email
        self.shopping_cart = ShoppingCart()

    def add_to_cart(self, product, quantity):
        self.shopping_cart.add_item(product, quantity)

    def view_cart(self):
        result = "Shopping cart:\n"
        for product, quantity in self.shopping_cart.items.items():
            result += f"{product} : {quantity}\n"
        return result.strip()