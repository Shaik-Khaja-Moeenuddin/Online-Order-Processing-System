from models.order import Order
from models.tracking import Tracking
from utils.validators import validate_quantity, validate_price
from json_storage.json_store import save_orders

orders = []

import matplotlib.pyplot as plt

def show_graph():
    if not orders:
        print("No data to display!")
        return

    products = []
    quantities = []

    for order in orders:
        products.append(order.product)
        quantities.append(order.quantity)

    plt.bar(products, quantities)
    plt.title("Product vs Quantity Ordered")
    plt.xlabel("Products")
    plt.ylabel("Quantity")

    plt.xticks(rotation=30)
    plt.tight_layout()
    plt.show()

def place_order():
    name = input("Enter customer name: ")
    product = input("Enter product: ")
    quantity = int(input("Enter quantity: "))
    price = float(input("Enter price: "))
    category = input("Enter category: ")

    if not validate_quantity(quantity):
        print("Invalid quantity!")
        return

    if not validate_price(price):
        print("Invalid price!")
        return

    order = Order(name, product, quantity, price, category)
    orders.append(order)

    print(f"\nOrder placed successfully!")
    print(f"Your Order ID: {order.order_id}")


def view_orders():
    if not orders:
        print("No orders available!")
        return

    for order in orders:
        order.display()


def update_status():
    oid = input("Enter Order ID: ")
    for order in orders:
        if order.order_id == oid:
            print("Statuses: Placed, Packed, Shipped, Delivered, Cancelled")
            status = input("Enter new status: ")
            order.update_status(status)
            print("Status updated successfully!")
            return

    print("Order not found!")


def tracking_system():
    tracking = Tracking()
    print(f"\nTracking ID: {tracking.tracking_id}")

    while True:
        update = input("Enter tracking update (or 'exit'): ")
        if update.lower() == "exit":
            break
        tracking.add_update(update)

    tracking.show_tracking()


def main():
    while True:
        print("\n===== ONLINE ORDER SYSTEM =====")
        print("1. Place Order")
        print("2. View Orders")
        print("3. Update Order Status")
        print("4. Tracking System")
        print("5. Show Graph")
        print("6. Save & Exit")


        choice = input("Enter your choice: ")

        if choice == '1':
            place_order()
        elif choice == '2':
            view_orders()
        elif choice == '3':
            update_status()
        elif choice == '4':
            tracking_system()
        elif choice == '5':
            show_graph()
        elif choice == '6':
            save_orders(orders)
            print("Data saved successfully. Exiting...")
            break


if __name__ == "__main__":
    main()