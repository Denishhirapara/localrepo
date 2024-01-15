import re
from datetime import datetime, timedelta


class Customer:
    def __init__(self, name, email, phone, street, city, state, country, company=None, type=None):

        list = [name, city, country, state]
        if any(any(char.isdigit() for char in name) for name in list):
            raise ValueError("------")

        if type not in ["company", "contact", "billing", "shipping"]:
            raise ValueError("Invalid customer type")

        if not phone.isdigit() or len(phone) != 10:
            raise ValueError("Invalid contact number")

        if not self.validate_email(email):
            raise ValueError("Invalid mail")

        self.name = name
        self.email = email
        self.phone = phone
        self.street = street
        self.city = city
        self.state = state
        self.country = country
        self.company = company
        self.type = type

    def validate_email(self, email):
        return bool(re.match(r'^\S+@\S+\.\S+$', email))

    def __str__(self):
        return (
            f"{self.name}    {self.email}     {self.phone}       {self.city}   {self.state}  {self.street}   {self.country}  {self.company}   {self.type}")


    def display(self):
        print(self)


class Product:
    def __init__(self,name,price):
        self.name=name
        self.price=price



    def __str__(self):
        return f"  product:{self.name}  price:{self.price} "

class Order:

    def __init__(self, number, date, company, billing, shipping, order_lines=None):

        if date < datetime.now():
            raise ValueError("Order date must be today or in the future")

        self.number = number
        self.date = date
        self.company = company
        self.billing = billing
        self.shipping = shipping
        self.order_lines = []

    def __str__(self):
        return (f" Oreder NO:{self.number} \n Date: {self.date} \n Company: {self.company} \n billinig:{self.billing} \n Shipping: {self.shipping}   ")

    def add_order_line(self, order_line):
        self.order_lines.append(order_line)

    def calculate_total_amount(self):
        total = sum(order_line.subtotal for order_line in self.order_lines)
        return total


    def display_order(self):
        for order_line in self.order_lines:
            print(f"  {order_line}")
        print(f"total: {ord1.calculate_total_amount()} ")

    def display_list(self, product):
        orders_for_product = [order_line.order for order_line in self.order_lines if product in order_line.products]
        if orders_for_product:
            print(f"{product.name}:")
            for order_for_product in orders_for_product:
                print(f"    Order {order_for_product.number} ")
            print()

    def order_by_date(self,order_list):
        n=len(order_list)
        for i in range(n):
            for j in range(i + 1, n):
                if order_list[j].date > order_list[i].date:
                    order_list[i], order_list[j] = order_list[j], order_list[i]

    def is_current_month(self):
        current_date = datetime.now()
        return self.date.month == current_date.month and self.date.year == current_date.year


    @classmethod
    def current_month_list(cls, order_list):
        current_month_orders = [order for order in order_list if order.is_current_month()]
        return current_month_orders

    def search_number(serlf,order_list):
        search=int(input("enter the number of order:"))
        for i in order_list:
            if i.number==search:
                print(f"  number: {i.number}   date: {i.date}  company:  {i.company}   billing:  {i.billing}   shipping: {i.shipping} ")



class OrderLine:
    def __init__(self, order,product, quantity, price):
        self.order=order
        self.products = product
        self.quantity = quantity
        self.price = price
        self.subtotal = sum(quantity * product.price for product in self.products)

    def __str__(self):
        product_str = "\n".join(str(product) for product in self.products)
        return f"{self.order} \n  {product_str} \n quentity: {self.quantity} \n Subtotal: {self.subtotal} "



    def calculate_amount(self):
        return self.subtotal


#five product object are created
pro1=Product("Tv",500)
pro2=Product("Ac",499)
pro3=Product("Basket",999)
pro4=Product("Bat",450)
pro5=Product("Laptop",250)

product_list=[pro1,pro2,pro3,pro4,pro5]

#five object are created customer
customer1 = Customer("Dharti Ent", "dharti@mail.com", "1259874563", "hirpara sheri", "bhunava", "gujarat", "ind", None, "billing")
customer2 = Customer("Sk Ent", "sk@mail.com", "1268563789", "kuvadva road", "gondal", "gujarat", "ind", None, "company")
customer3 = Customer("Nilkanth Ent", "nilkanth@mail.com", "1224489756", "green pan near", "rajapara", "gujarat", "ind", None, "billing")
customer4 = Customer("Decora Ent", "decora@mail.com", "7894567890", "panchayat chowk", "kuvadava", "gujarat", "ind", None, "shipping")
customer5 = Customer("Pooja Ent", "pooja@mail.com", "4589623542", "vijay ploat", "jamnagar", "gujarat", "ind", None, "company")

custom_list=[customer1,customer2,customer3,customer4,customer5]

#five order object are created
ord1 = Order(12540, datetime(2024, 1, 25), customer1, customer1, customer2, [])
ord2 = Order(32450, datetime(2024, 5, 15), customer3, customer5, customer2, [])
ord3 = Order(82650, datetime(2024, 1, 21), customer4, customer2, customer5, [])
ord4 = Order(52550, datetime(2024, 6, 12), customer1, customer4, customer2, [])
ord5 = Order(62850, datetime(2024, 8, 16), customer3, customer4, customer2, [])



order_line1 = OrderLine(ord1,[pro1], 4, 0)
order_line2 = OrderLine(ord2,[pro3], 3, 0)
order_line3 = OrderLine(ord3,[pro1], 4, 0)
order_line4 = OrderLine(ord4,[pro5], 1, 0)
order_line5 = OrderLine(ord5,[pro1], 5, 0)



#add orderlines one by one in orderlines list
ord1.add_order_line(order_line1)
ord1.add_order_line(order_line2)
ord1.add_order_line(order_line3)
ord1.add_order_line(order_line4)
ord1.add_order_line(order_line5)


ord_list=[ord1,ord2,ord3,ord4,ord5]

#print the order details
print("---order details---")
ord1.display_order()


print("---list of all order by specific product---")
products_to_search = [pro1, pro2,pro3,pro4,pro5]


for product in products_to_search:
    for order in ord_list:
        order.display_list(product)



print("---get the order_by_date---")
ord1.order_by_date(ord_list)
for i in ord_list:
    print(f"  number: {i.number}   date: {i.date}  company:  {i.company}   billing:  {i.billing}   shipping: {i.shipping} ")



print("---get the current_month---")
current_month_orders = Order.current_month_list(ord_list)
for order in current_month_orders:
    print(f"  number: {order.number}   date: {order.date}  company:  {order.company}   billing:  {order.billing}   shipping: {order.shipping} ")


print("---get the search order by numbers---")
ord1.search_number(ord_list)