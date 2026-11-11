from user import User

class Privileges:
    """A class to store an admin's privileges."""

    def __init__(self, privileges=None):
        if privileges is None:
            privileges = ['can add post', 'can delete post', 'can ban user']
        self.privileges = privileges

    def show_privileges(self):
        print("\nPrivileges:")
        for privilege in self.privileges:
            print(f"- {privilege}")


class Admin(User):
    """Represent an admin user."""

    def __init__(self, first_name, last_name, username, email):
        super().__init__(first_name, last_name, username, email)
        self.privileges = Privileges()