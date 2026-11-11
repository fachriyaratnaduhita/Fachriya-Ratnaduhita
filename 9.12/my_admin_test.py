from admin_privileges import Admin

# Membuat instance dan menguji
admin_user = Admin('siti', 'rahma', 'srahma', 'siti@admin.com')
admin_user.describe_user()
admin_user.privileges.show_privileges()