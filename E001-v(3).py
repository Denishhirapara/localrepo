class Category:
    def __init__(self, name, code, parent=None):
        self.name = name
        self.code = code
        self.parent = parent
        self.products = []

    def __str__(self):
        return f"{self.name} {self.code} {(self.products)}"


class Product:
    def __init__(self, name, code, category, price, stock_at_locations):
        self.name = name
        self.code = code
        self.category = category
        self.price = price
        self.stock_at_locations = stock_at_locations

    def __str__(self):
        locations = '   -->>   '.join([f"{location.name} ({location.code}): {quantity}" for location, quantity in self.stock_at_locations.items()])
        return f"Product name: {self.name}  Code: {self.code}  Category: {self.category.name}  Price: {self.price}  Stock at Locations: {locations}"

    def move(self, from_location, to_location, quantity):
        try:
            if self.stock_at_locations[from_location] >= quantity:

                new_movement = Movement(from_location, to_location, self, quantity)

                Movement.movements_list.append(new_movement)


                self.stock_at_locations[from_location] -= quantity

                if to_location in self.stock_at_locations:

                    self.stock_at_locations[to_location] += quantity
                else:

                    self.stock_at_locations[to_location] = quantity

                # Print a success message
                print(f"Move {quantity} units of {self.name} from {from_location.name} to {to_location.name}")
            else:

                raise ValueError(f"stock is not avilable")
        except KeyError:

            raise ValueError(f"stock is not avilable")
    @staticmethod
    def display_details(self):
        print(self)
        print()


    @classmethod
    def stock_information(self,location_list, product_list):
        for location in location_list:
            print(f"{location.name}:")
            location_products = [product for product in pro_list if location in product.stock_at_locations]
            for product in location_products:
                print(f"  {product.name} ({product.code}): {product.stock_at_locations[location]}")
            print()


class Location:
    def __init__(self, name, code):
        self.name = name
        self.code = code

    def __str__(self):
        return f"{self.name} {self.code}"


class Movement:
    movements_list = []

    def __init__(self, from_location, to_location, product, quantity):
        self.from_location = from_location
        self.to_location = to_location
        self.product = product
        self.quantity = quantity


    def __str__(self):
        return f"{self.from_location}  {self.to_location}  {self.product}  {self.quantity}"

    @staticmethod
    def movements_by_product(product):
        return [movement for movement in Movement.movements_list if movement.product == product]

    @classmethod
    def product_movements(self,product):
        for product in pro_list:
            movements = set(Movement.movements_by_product(product))
            print(f"Product: {product.name} ({product.code})")
            for movement in movements:
                    print(f"  {movement}")
                    print()


# Creating categories
vehicle = Category("Creta", 1014)
car = Category("Verna", 1015, parent=vehicle)
petrol = Category("City", 1016, parent=car)
metro = Category("Odii", 1017, parent=petrol)
railway = Category("I20", 1018, parent=metro)

# Creating locations
loc1 = Location("Kanpur", 2012)
loc2 = Location("Baroda", 2013)
loc3 = Location("Gondal", 2014)
loc4 = Location("Surat", 2015)

# Creating products
product20 = Product("Product20", 1125, petrol, 450, {loc1: 45})
product21 = Product("Product21", 1055, vehicle, 540, {loc2: 13})
product22 = Product("Product22", 1452, car, 700, {loc3: 23})
product23 = Product("Product23", 1305, railway, 250, {loc4: 15})
product24 = Product("Product24", 6310, metro, 100, {loc1: 20})

pro_list= [product20, product21, product22, product23, product24]

loc_list=[loc1,loc2,loc3,loc4]
# Displaying product details

print("---display details---")
for product in pro_list:
    Product.display_details(product)

print(" ")


# Moving products from one location to another
product20.move(loc1, loc2,5)
product21.move(loc2, loc3, 7);
product22.move(loc3, loc4, 10)
product23.move(loc4, loc1, 9)
product24.move(loc1, loc3, 3)

# Displaying movements of each product
print("----updat stock at locations -----")

product20.stock_information(loc_list,pro_list)

print("---movement all detail---")

Movement.product_movements(product)
