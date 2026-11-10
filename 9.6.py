class Restaurant:
    """A simple attempt to model a restaurant."""

    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type

    def describe_restaurant(self):
        print(f"{self.restaurant_name} serves wonderful {self.cuisine_type} food.")


class IceCreamStand(Restaurant):
    """Represent an ice cream stand, inheriting from Restaurant."""

    def __init__(self, restaurant_name, cuisine_type='ice cream'):
        """Initialize attributes of the parent class, plus flavors."""
        super().__init__(restaurant_name, cuisine_type)
        self.flavors = ['vanilla', 'chocolate', 'strawberry', 'mint chocolate chip']

    def display_flavors(self):
        """Display the available ice cream flavors."""
        print("\nWe have the following ice cream flavors available:")
        for flavor in self.flavors:
            print(f"- {flavor.title()}")

# Creating an instance and calling the method
my_ice_cream_stand = IceCreamStand("Sweet Scoops")
my_ice_cream_stand.describe_restaurant()
my_ice_cream_stand.display_flavors()