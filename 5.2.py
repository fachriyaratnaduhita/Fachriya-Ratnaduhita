# Tests for equality and inequality with strings
food = 'pizza'
print(food.lower() == 'Pizza')  
print(food != 'burger') 
print(food == 'Burger') 

# Tests using the lower() method
name = 'john'
print(name.lower() == 'john') 
print(name.lower() == 'Mary')

# Numerical tests
number = 15
print(number == 15)  
print(number != 10)  
print(number > 20) 
print(number < 20 )
print(number >= 15)  
print(number <= 10) 

# Tests using 'and' and 'or' keywords
age_0 = 22
age_1 = 18
print(age_0 >= 21 and age_1 >= 21)
print(age_0 >= 21 or age_1 >= 21) 

# Test whether an item is in a list
colors = ['red', 'green', 'blue']
print('green' in colors) 
print('yellow' in colors) 

# Test whether an item is not in a list
banned_users = ['andrew', 'carolina', 'david']
print('marie' not in banned_users) 
print('andrew' not in banned_users) 