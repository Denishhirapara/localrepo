class category:
    def __init__(self, name, code,parent=None):
        self.name = name
        self.code = code
        self.no_of_products=0


        self.parent=parent
        self.display_name=self.dis_name()
        self.products=[]

#this function use for print the object

    def __str__(self):
        return f"{self.name} {self.code} {self.no_of_products}"
#add new product
    def add_product(self, pro):
        self.products.append(pro)

#generate display name
    def dis_name(self):
        if self.parent:
            return f"{self.parent.display_name} > {self.name}"
        else:
            return self.name

#display details of name ,code, display name,no of products etc
    def display_details(self):
        print(f"Category Code:{self.name} ({self.code})")
        print(f"Display Name: {self.display_name}")
        print(f"No. of products: {self.no_of_products}")

        for product in self.products:
            print(f"  name:  {product.name}    code:  {product.code}    price:  {product.price}")
        print()


class product:
    def __init__(self, name, code, category, price):
        self.name = name
        self.code = code
        self.category = category
        self.price = price

#get the product price
    # def get_price(self):
    #     return self.price

# get the category name
#     def get_name(self):
#         return self.category.name

#sort the product list by category name
    def sort_products_by_name(self,pro_list):
        n = len(pro_list)
        for i in range(n - 1):
            for j in range(0, n - i - 1):
                if pro_list[j].category.name > pro_list[j + 1].category.name:
                    pro_list[j], pro_list[j + 1] = pro_list[j + 1], pro_list[j]

#low to high price
    def Lsort(self,pro_list):
        n = len(pro_list)
        for i in range(n):
            for j in range(i + 1, n):
                if pro_list[j].price < pro_list[i].price:
                    pro_list[i], pro_list[j] = pro_list[j], pro_list[i]

#high to low price
    def Hsort(self,h):
        n = len(h)
        for i in range(n):
            for j in range(i + 1, n):
                if h[j].price > h[i].price:
                    h[i], h[j] = h[j], h[i]

#search product by code
    def search(self,pro_list):
            se = int(input("Enter the code: "))
            for i in pro_list:
                if i.code == se:
                    print(f"Name:  {i.name}   Code: {i.code}  Category: {i.category}  price: {i.price}")


#5 category object
vehicle =category("amresider", 104)
car =category("scorpio", 15,parent=vehicle)
petrol =category("camrige", 101,parent=car)
bullet=category("enduver",7,parent=petrol)
honda=category("forchu",80,parent=bullet)

#3 object category
metro= category("bugati", 10511)
brezza= category("city", 5489)
railway= category("verna", 8956)


category_list=[vehicle,car,petrol,bullet,honda,brezza,metro,railway]

#10 product
product1 = product("ab", 101, bullet, 100)
product2 = product("bc", 100, brezza, 1100)
product3 = product("cd", 101, honda, 10)
product4 = product("de", 122, bullet, 1940)
product5 = product("ef", 103, brezza, 1060)
product6 = product("gh", 104, bullet, 190)
product7 = product("jk", 5, honda, 780)
product8 = product("ll", 106, bullet, 630)
product9 = product("ms", 107, brezza, 3)
product10 = product("bn", 102, honda, 9)

#create 3 product object for each category
product11 = product("ld",109, car, 4)
product12 = product("ai",130, car, 11)
product13 = product("ml",10, car, 350)

product14 = product("pq",32, vehicle, 85)
product15 = product("pg",13, vehicle, 80)
product16 = product("ql",1040, vehicle, 5900)

product17 = product("sq",105, petrol, 587)
product18 = product("dd",160, petrol, 49)
product19 = product("mm",17, petrol, 45)

#add the new category in product list
vehicle.add_product(product11)
vehicle.add_product(product12)
vehicle.add_product(product13)

car.add_product(product14)
car.add_product(product15)
car.add_product(product16)

petrol.add_product(product17)
petrol.add_product(product18)
petrol.add_product(product19)

#
# bullet.add_product(product1)
# bullet.add_product(product4)
# bullet.add_product(product6)
#
# honda.add_product(product3)
# honda.add_product(product7)
# honda.add_product(product10)


pro_list = [product1, product2, product3, product4, product5, product6, product7, product8,
                product9, product10,product11,product12,product13,product14,product15,product16,
                product17,product18,product19]


product1.Lsort(pro_list)

#update the product list
for pro in pro_list:
    pro.category.no_of_products+=1


# Print category info with its no_of_products
print("<.... Print category with its no of products..>")
for category in category_list:
    print(f" Name:  {category.name}  Code:  {category.code}  NO_of_product:  {category.no_of_products}")

print()

#  low to high price
print(" <......low to high price.....>")

product1.Lsort(pro_list)


for pro in pro_list:
    print(f"Name:  {pro.name}  Code:  {pro.code}  Category:  {pro.category}  price:  {pro.price}")


print()

#high to low price

print(" <......high to low price......>")
product1.Hsort(pro_list)
for pro in pro_list:
    print(f"Name:  {pro.name}   Code:  {pro.code}  Category:  {pro.category}  price:  {pro.price}")

print()

#display details
for category in category_list:
    category.display_details()

print()

#product list by order by category name
print("<.....product list order by category.....>")
product1.sort_products_by_name(pro_list)
for pro in pro_list:
    print(f"Name:  {pro.name}   Code:  {pro.code}  Category:  {pro.category}  price:  {pro.price}")

print()

#Search product by code
print("<....Searching product by code.....>")

product1.search(pro_list)

