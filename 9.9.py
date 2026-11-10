class Car:
    """A simple attempt to represent a car."""

    def __init__(self, manufacturer, model, year):
        self.manufacturer = manufacturer
        self.model = model
        self.year = year
        self.odometer_reading = 0

    def get_descriptive_name(self):
        long_name = f"{self.year} {self.manufacturer} {self.model}"
        return long_name.title()


class Battery:
    """A attempt to model a battery for an electric car."""

    def __init__(self, battery_size=40):
        self.battery_size = battery_size

    def describe_battery(self):
        print(f"This car has a {self.battery_size}-kWh battery.")

    def get_range(self):
        """Print a statement about the range this battery provides."""
        if self.battery_size == 40:
            range_miles = 150
        elif self.battery_size == 65:
            range_miles = 225

        print(f"This car can go about {range_miles} miles on a full charge.")

    def upgrade_battery(self):
        """Check the battery size and upgrade it if possible."""
        if self.battery_size != 65:
            self.battery_size = 65
            print("Upgraded the battery to 65 kWh.")
        else:
            print("The battery is already upgraded.")


class ElectricCar(Car):
    """Represent aspects of a car, specific to electric vehicles."""

    def __init__(self, manufacturer, model, year):
        super().__init__(manufacturer, model, year)
        self.battery = Battery()


# Membuat mobil listrik dengan baterai bawaan (default 40 kWh)
my_electric_car = ElectricCar('nissan', 'leaf', 2024)

print(my_electric_car.get_descriptive_name())
my_electric_car.battery.describe_battery()
my_electric_car.battery.get_range()

# Melakukan upgrade baterai
print("\nChecking and upgrading battery:")
my_electric_car.battery.upgrade_battery()
my_electric_car.battery.get_range()