from Order import Order
from Product import Product
from User import User
from Warehouse import Warehouse

warehouse = Warehouse()
apple = Product("Apple", "Fresh Red Apple", 0.5) # name, description, price
banana = Product("Banana", "Fresh Yellow Banana", 0.3)

# Add products to warehouse
warehouse.add_product(apple, 100)  # 100 apples in warehouse
warehouse.add_product(banana, 150)  # 150 bananas in warehouse

# Create a user
user = User("John Doe", "john.doe@example.com")

# User adds items to cart
user.add_to_cart(apple, 5)
user.add_to_cart(banana, 10)


print(user.view_cart()) # Output: Apple: 5, Banana: 10

# User places an order
order = Order(user, warehouse)
order.place_order()

# User views items in cart after order is placed (should be empty)
print(user.view_cart()) # Output: None

# View stock after order is placed
print(warehouse.view_stock()) # Output: Apple: 95, Banana: 140