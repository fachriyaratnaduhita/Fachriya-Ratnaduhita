class Restaurant:
    """A simple attempt to model a restaurant."""

    def __init__(self, restaurant_name, cuisine_type):
        """Initialize restaurant name and cuisine type."""
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type

    def describe_restaurant(self):
        """Display a summary of the restaurant."""
        print(f"{self.restaurant_name} serves wonderful {self.cuisine_type} food.")

    def open_restaurant(self):
        """Display a message that the restaurant is open."""
        print(f"{self.restaurant_name} is now open!")

# Creating an instance
restaurant = Restaurant('gourmet palace', 'italian')

# Printing attributes individually
print(restaurant.restaurant_name)
print(restaurant.cuisine_type)

# Calling methods
restaurant.describe_restaurant()
restaurant.open_restaurant()