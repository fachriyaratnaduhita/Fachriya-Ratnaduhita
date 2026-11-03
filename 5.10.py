current_users = ['Dika', 'Ella', 'Tata', 'Christa', 'Azalia']
new_users = ['Dika', 'Tata', 'Zaskia', 'Tiwi', 'Putri']

# Convert current_users to lowercase to make case-insensitive comparison reliable
current_users_lower = [user.lower() for user in current_users]

for new_user in new_users:
    if new_user in current_users:
        print(f"you will need to enter a new username!")
    else:
        print("the username is available.")