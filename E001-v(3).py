class product:
    def __init__(self, name, code, category, price,stock_at_locations):
        self.name = name
        self.code = code
        self.category = category
        self.price = price
        self.stock_at_location = stock_at_locations

    def __str__(self):
        return f"{self.name} {self.code} {self.category}  {self.price}  {self.stock_at_location}"


#create one class name locaiton
class Location():
    def __init__(self,name,code):
        self.name=name
        self.code=code

    def __str__(self):
        return f"{self.name}  {self.code}"



#create one class name movement
class movement():
    movement_list=[]
    def __init__(self,from_location,to_location,product,quantity):
        self.from_location=from_location
        self.to_location=to_location
        self.product=product
        self.quantity=quantity
        # movement.movement_list.append(self)

    def  __str__(self):
        return f"{self.from_location}  {self.to_location}  {self.product}  {self.quantity}"

#create a static method
    def movements_by_product(product):
         return [movement for movement in movement.movement_list if movement.product == product]


# Create 4 different location objects
man1 = Location("amreli", 1)
man2 = Location("gondal", 2)
man3 = Location("bagasara", 3)
man4 = Location("rajkot", 4)

# five different product object

pro1 = product("laptop","g2","cate1",50000,{man1: 56,man2: 2,man3: 80,man4: 35})
pro2 = product("keyboard","a1","cate2",400,{man1: 5,man2: 50,man3: 8,man4: 45})
pro3 = product("mouce","m2","cate3",105,{man1: 75,man2: 300,man3: 31,man4: 95})
pro4 = product("iphone","ip6","cate4",45000,{man1: 6,man2: 23,man3: 10,man4: 3})
pro5 = product("camera","c7","cate5",120000,{man1: 9,man2: 52,man3 : 0,man4: 61})

pro_list = [pro1,pro2,pro3,pro4,pro5]
loc_list = [man1,man2,man3,man4]

# create four different movement objects

mov1 = movement("location1","location2","product1",50)
mov2 = movement("location2","location3","product4",50)
mov3 = movement("location3","location4","product5",50)
mov4 = movement("location4","location1","product2",50)
mov4 = movement("location1","location3","product2",50)


#print the product_list

for product in pro_list:
    product_movements = movement.movements_by_product(product)
    print(f"{product.name} ({product.code}):")

    for movement in product_movements:
        print(f"  -From-  {movement.from_location.name} To- {movement.to_location.name} Stock- {movement.quantity}")
print()

for product in pro_list:
    print(f"{product.name} ({product.code}):")

    for location, stock in product.stock_at_location.items():
        print(f"  From--   {location.name}  Stock--  {stock}")

# for location in [pro1, pro2, pro3, pro4]:
#     print(f"{location.name} ({location.code}):")
#     for product in [pro1, pro2, pro3, pro4, pro5]:
#         if location in product.stock_at_location:
#             stock = product.stock_at_location[location]
#             print(f"  {product.name} ({product.code}) - Stock: {stock}")




