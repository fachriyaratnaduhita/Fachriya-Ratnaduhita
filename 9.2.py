class Restaurant:
    """A simple attempt to model a restaurant."""

    def __init__(self, restaurant_name, cuisine_type):
        """Initialize restaurant name and cuisine type."""
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type

    def describe_restaurant(self):
        """Display a summary of the restaurant."""
        print(f"{self.restaurant_name.title()} serves wonderful {self.cuisine_type.title()} food.")

    def open_restaurant(self):
        """Display a message that the restaurant is open."""
        print(f"{self.restaurant_name.title()} is now open!")

# Membuat 3 instance (objek) yang berbeda dari kelas Restaurant
restaurant_1 = Restaurant('gourmet palace', 'italian')
restaurant_2 = Restaurant('spice garden', 'indian')
restaurant_3 = Restaurant('sushi bar', 'japanese')

# Memanggil metode describe_restaurant() untuk masing-masing instance
restaurant_1.describe_restaurant()
restaurant_2.describe_restaurant()
restaurant_3.describe_restaurant()