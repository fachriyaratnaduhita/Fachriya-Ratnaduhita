usernames = ['admin', 'James', 'Tika', 'Kania', 'Vita']
for username in usernames:
    if 'admin' in username:
        print("Hello admin, would you like to see a status report?")
    else:
        print(f"Hello {username}, thank you for your logging in again!")

