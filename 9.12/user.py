class User:
    """Represent a user profile."""

    def __init__(self, first_name, last_name, username, email):
        self.first_name = first_name
        self.last_name = last_name
        self.username = username
        self.email = email

    def describe_user(self):
        print(f"User: {self.username} ({self.first_name} {self.last_name})")