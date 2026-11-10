class User:
    """Represent a user profile."""

    def __init__(self, first_name, last_name, username, email):
        self.first_name = first_name
        self.last_name = last_name
        self.username = username
        self.email = email

    def describe_user(self):
        print(f"User: {self.username} ({self.first_name} {self.last_name})")


class Admin(User):
    """Represent an admin user with special privileges."""

    def __init__(self, first_name, last_name, username, email):
        """Initialize parent attributes and admin privileges."""
        super().__init__(first_name, last_name, username, email)
        self.privileges = ['can add post', 'can delete post', 'can ban user']

    def show_privileges(self):
        """Display the administrator's privileges."""
        print(f"\nPrivileges for admin {self.username}:")
        for privilege in self.privileges:
            print(f"- {privilege}")

# Creating an instance and calling the method
admin_user = Admin('alice', 'smith', 'asmith', 'alice@admin.com')
admin_user.describe_user()
admin_user.show_privileges()