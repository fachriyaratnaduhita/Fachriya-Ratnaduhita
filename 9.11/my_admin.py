from user_admin import Admin

# Membuat instance Admin
super_admin = Admin('budi', 'santoso', 'bsantoso', 'budi@admin.com')

# Menguji metode
super_admin.describe_user()
super_admin.privileges.show_privileges()