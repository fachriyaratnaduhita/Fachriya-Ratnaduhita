class Restaurant:
    """A simple attempt to model a restaurant."""

    def __init__(self, restaurant_name, cuisine_type):
        """Initialize restaurant name, cuisine type, and number served."""
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        self.number_served = 0  # Atribut baru dengan nilai default 0

    def describe_restaurant(self):
        """Display a summary of the restaurant."""
        print(f"{self.restaurant_name.title()} serves wonderful {self.cuisine_type.title()} food.")

    def open_restaurant(self):
        """Display a message that the restaurant is open."""
        print(f"{self.restaurant_name.title()} is now open!")

    def set_number_served(self, number):
        """Set the number of customers that have been served."""
        self.number_served = number

    def increment_number_served(self, additional_customers):
        """Add the given amount to the number of customers served."""
        self.number_served += additional_customers


# Membuat instance bernama restaurant
restaurant = Restaurant('gourmet palace', 'italian')

# 1. Mencetak nilai default number_served
print(f"Number of customers served: {restaurant.number_served}")

# 2. Mengubah nilai atribut secara langsung lalu mencetaknya kembali
restaurant.number_served = 45
print(f"Number of customers served (updated directly): {restaurant.number_served}")

# 3. Menggunakan metode set_number_served() untuk mengatur angka baru
restaurant.set_number_served(150)
print(f"Number of customers served (using set method): {restaurant.number_served}")

# 4. Menggunakan metode increment_number_served() untuk menambah jumlah pelanggan harian
restaurant.increment_number_served(75)
print(f"Number of customers served (after incrementing): {restaurant.number_served}")