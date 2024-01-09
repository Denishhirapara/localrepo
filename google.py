class Location:
    def __init__(self, name, code):
        self.name = name
        self.code = code

class Movement:
    movement_list = []

    def __init__(self, from_location, to_location, product, quantity):
        self.from_location = from_location
        self.to_location = to_location
        self.product = product
        self.quantity = quantity
        Movement.movement_list.append(self)

    @staticmethod
    def movements_by_product(product):
        return [movement for movement in Movement.movement_list if movement.product == product]

class Product:
    def __init__(self, name, code, stock_at_locations=None):
        self.name = name
        self.code = code
        self.stock_at_locations = stock_at_locations if stock_at_locations is not None else {}

# Create 4 different location objects
location1 = Location("Location A", 1)
location2 = Location("Location B", 2)
location3 = Location("Location C", 3)
location4 = Location("Location D", 4)

# Create 5 different product objects
product1 = Product("Product 1", "P1")
product2 = Product("Product 2", "P2")
product3 = Product("Product 3", "P3")
product4 = Product("Product 4", "P4")
product5 = Product("Product 5", "P5")

# Move those 5 products from one location to another location using movement.
# Manage exceptions if product stock goes negative.
movements = [
    Movement(location1, location2, product1, 20),
    Movement(location3, location4, product2, 15),
    Movement(location2, location3, product3, 10),
    Movement(location4, location1, product4, 25),
    Movement(location1, location3, product5, 30),
]

# Display movements of each product using the “movements_by_product” method.
print("Movements by Product:")
for product in [product1, product2, product3, product4, product5]:
    product_movements = Movement.movements_by_product(product)
    print(f"{product.name} ({product.code}):")
    for movement in product_movements:
        print(f"  From {movement.from_location.name} to {movement.to_location.name} - Quantity: {movement.quantity}")

# Display product details with its stock at various locations using “stock_at_locations”.
print("\nProduct details with Stock at Locations:")
for product in [product1, product2, product3, product4, product5]:
    print(f"{product.name} ({product.code}):")
    for location, stock in product.stock_at_locations.items():
        print(f"  {location.name} - Stock: {stock}")

# Display product list by location (group by location)
print("\nProduct list by Location:")
for location in [location1, location2, location3, location4]:
    print(f"{location.name} ({location.code}):")
    for product in [product1, product2, product3, product4, product5]:
        if location in product.stock_at_locations:
            stock = product.stock_at_locations[location]
            print(f"  {product.name} ({product.code}) - Stock: {stock}")
