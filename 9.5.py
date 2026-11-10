class User:
    """Represent a user profile with login attempts tracking."""

    def __init__(self, first_name, last_name, username, email, location):
        """Initialize user attributes, including login_attempts set to 0."""
        self.first_name = first_name
        self.last_name = last_name
        self.username = username
        self.email = email
        self.location = location
        self.login_attempts = 0  # Atribut baru dengan nilai default 0

    def describe_user(self):
        """Print a summary of the user's information."""
        print(f"\nUser Profile: {self.username}")
        print(f"Name: {self.first_name.title()} {self.last_name.title()}")
        print(f"Email: {self.email}")
        print(f"Location: {self.location.title()}")

    def greet_user(self):
        """Print a personalized greeting to the user."""
        print(f"Welcome back, {self.first_name.title()}!")

    def increment_login_attempts(self):
        """Increment the value of login_attempts by 1."""
        self.login_attempts += 1

    def reset_login_attempts(self):
        """Reset login_attempts back to 0."""
        self.login_attempts = 0


# 1. Membuat instance dari kelas User
user_1 = User('john', 'doe', 'johndoe', 'johndoe@email.com', 'new york')

# 2. Memanggil increment_login_attempts() beberapa kali
user_1.increment_login_attempts()
user_1.increment_login_attempts()
user_1.increment_login_attempts()

# 3. Mencetak nilai login_attempts untuk memastikan bertambah
print(f"Login attempts: {user_1.login_attempts}")

# 4. Mereset nilai login_attempts menjadi 0
user_1.reset_login_attempts()

# 5. Mencetak kembali untuk memastikan sudah tereset
print(f"Login attempts after reset: {user_1.login_attempts}")