def build_profile(first, last, **user_info):
    """Build a dictionary containing everything we know about a user."""
    user_info['first_name'] = first
    user_info['last_name'] = last
    return user_info

my_profile = build_profile(
    'fachriya', 'ratnaduhita',
    location='surakarta',
    field='physics',
    hobby='listening to music'
)

print(my_profile)