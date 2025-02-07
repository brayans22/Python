"""EXERCISE 1"""

supermarket_products = [
    {"name": "apple", "price": 0.5},
    {"name": "apple", "price": 0.5},
    {"name": "bread", "price": 1},
    {"name": "milk", "price": 2},
    {"name": "sugar", "price": 0.2},
    {"name": "water", "price": 1},
    {"name": "bacon", "price": 0.95},
    {"name": "milk", "price": 2}
]


def show_ticket(products):
    """Function that generates a supermarket ticket"""
    count_products = {}
    total = 0

    for product in products:
        name_product = product["name"]
        if name_product in count_products:
            count_products[name_product]["count"] += 1
        else:
            count_products[name_product] = {
                "price": product["price"], "count": 1}

    print("-------------------")
    print("Ticket")
    print("-------------------")

    for name, info in count_products.items():
        total_price_product = info["price"] * info["count"]
        total += total_price_product
        print(f"{name} x{info['count']} - ${total_price_product:.2f}")

    print("-------------------")
    print(f"Total: ${total}")
    print("-------------------")


show_ticket(supermarket_products)
