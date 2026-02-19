class User:
    users_db = {}

    def __init__(self, user_id, name, email):
        
        self.user_id = user_id
        self.name = name
        self.email = email

    
    def save(self):
        User.users_db[self.user_id] = {
            "name": self.name,
            "email": self.email
        }
        print("User stored")

    
    @classmethod
    def get_user(cls,user_id):
        return cls.users_db.get(user_id)

  
    @classmethod
    def update_user(cls, user_id, name=None, email=None):
        if user_id in cls.users_db:
            if name:
                cls.users_db[user_id]["name"] = name
            if email:
                cls.users_db[user_id]["email"] = email
            print("User updated")

    
    @classmethod
    def delete_user(cls, user_id):
        if user_id in cls.users_db:
            del cls.users_db[user_id]
            print("User deleted")

    @classmethod
    def show_all(cls):
        return cls.users_db



class Product:
    products_db = {}

    def __init__(self, product_id, name, price):
        self.product_id = product_id
        self.name = name
        self.price = price

    def save(self):
        Product.products_db[self.product_id] = {
            "name": self.name,
            "price": self.price
        }
        print("Product stored")

    @classmethod
    def get_product(cls, product_id):
        return cls.products_db.get(product_id)

    @classmethod
    def update_product(cls, product_id, name=None, price=None):
        if product_id in cls.products_db:
            if name:
                cls.products_db[product_id]["name"] = name
            if price:
                cls.products_db[product_id]["price"] = price
            print("Product updated")

    @classmethod
    def delete_product(cls, product_id):
        if product_id in cls.products_db:
            del cls.products_db[product_id]
            print("Product deleted")

    @classmethod
    def show_all(cls):
        return cls.products_db



class Order:
    orders_db = {}

    def __init__(self, order_id, user_id):
        self.order_id = order_id
        self.user_id = user_id
        self.items = []
        self.total = 0

    def add_product(self, product_id, qty):
        product = Product.products_db.get(product_id)
        if product:
            price = product["price"]
            self.items.append({
                "product_id": product_id,
                "qty": qty,
                "price": price
            })
            self.total += price * qty
            print("Item added")
        else:
            print("Product not found")

    def place_order(self):
        Order.orders_db[self.order_id] = {
            "user_id": self.user_id,
            "items": self.items,
            "total": self.total
        }
        print("Order stored")

    @classmethod
    def get_order(cls, order_id):
        return cls.orders_db.get(order_id)

    @classmethod
    def delete_order(cls, order_id):
        if order_id in cls.orders_db:
            del cls.orders_db[order_id]
            print("Order deleted")

    @classmethod
    def show_all(cls):
        return cls.orders_db
    

u1 = User(1, "Mrudula", "m@gmail.com")
u1.save()

p1 = Product(101, "Kurti", 500)
p1.save()

p2 = Product(102, "Saree", 1200)
p2.save()

o1 = Order(5001, 1)
o1.add_product(101, 2)
o1.add_product(102, 1)
o1.place_order()

print("\nUsers:", User.show_all())
print("Products:", Product.show_all())
print("Orders:", Order.show_all())    

   


