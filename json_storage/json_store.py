import json

FILE = "orders.json"

def save_orders(order_list):
    data = []
    for o in order_list:
        data.append(o.to_dict())

    with open(FILE, "w") as f:
        json.dump(data, f, indent=4)

def load_orders():
    try:
        with open(FILE, "r") as f:
            return json.load(f)
    except:
        return []