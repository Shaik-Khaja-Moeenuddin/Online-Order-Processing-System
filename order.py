import uuid
from models.record import Record

class Order(Record):
    def __init__(self, customer, product, quantity, price, category):
        super().__init__()
        self.order_id = str(uuid.uuid4())[:8]
        self.customer = customer
        self.product = product
        self.quantity = quantity
        self.price = price
        self.category = category
        self.status = "Placed"

    def calculate_total(self):
        return self.quantity * self.price

    def update_status(self, status):
        self.status = status

    def to_dict(self):
        return {
            "order_id": self.order_id,
            "customer": self.customer,
            "product": self.product,
            "quantity": self.quantity,
            "price": self.price,
            "category": self.category,
            "status": self.status
        }

    def display(self):
        print("\n----------------------------")
        print(f"Order ID   : {self.order_id}")
        print(f"Customer   : {self.customer}")
        print(f"Product    : {self.product}")
        print(f"Quantity   : {self.quantity}")
        print(f"Price      : {self.price}")
        print(f"Category   : {self.category}")
        print(f"Status     : {self.status}")
        print(f"Total Cost : {self.calculate_total()}")
        print("----------------------------")