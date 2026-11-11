class User:
    """Represent a user profile."""

    def __init__(self, first_name, last_name, username, email):
        self.first_name = first_name
        self.last_name = last_name
        self.username = username
        self.email = email

    def describe_user(self):
        print(f"User: {self.username} ({self.first_name} {self.last_name})")


class Privileges:
    """A class to store an admin's privileges."""

    def __init__(self, privileges=None):
        if privileges is None:
            privileges = ['can add post', 'can delete post', 'can ban user']
        self.privileges = privileges

    def show_privileges(self):
        """Display the administrator's privileges."""
        print("\nPrivileges:")
        for privilege in self.privileges:
            print(f"- {privilege}")


class Admin(User):
    """Represent an admin user using a Privileges instance."""

    def __init__(self, first_name, last_name, username, email):
        super().__init__(first_name, last_name, username, email)
        self.privileges = Privileges()