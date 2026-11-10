class User:
    """Represent a user profile."""

    def __init__(self, first_name, last_name, username, email, location):
        """Initialize user attributes."""
        self.first_name = first_name
        self.last_name = last_name
        self.username = username
        self.email = email
        self.location = location

    def describe_user(self):
        """Print a summary of the user's information."""
        print(f"\nUser Profile: {self.username}")
        print(f"Name: {self.first_name.title()} {self.last_name.title()}")
        print(f"Email: {self.email}")
        print(f"Location: {self.location.title()}")

    def greet_user(self):
        """Print a personalized greeting to the user."""
        print(f"Welcome back, {self.first_name.title()}!")

# Creating instances
user_1 = User('john', 'doe', 'johndoe', 'johndoe@email.com', 'new york')
user_2 = User('sarah', 'conner', 'sconner', 'sarah@email.com', 'los angeles')

# Calling methods for each user
user_1.describe_user()
user_1.greet_user()

user_2.describe_user()
user_2.greet_user()