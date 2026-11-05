def make_sandwich(item, *toppings):
    """Summarize the sandwich being ordered."""
    print(f"\nMaking {item} sandwiches with the following toppings:")
    for topping in toppings:
        print(f"- {topping}")

make_sandwich(5, 'egg', 'lettuce', 'ham')
make_sandwich(10, 'sausage', 'cheese')
make_sandwich(34, 'peanut butter', 'strawberry jam')