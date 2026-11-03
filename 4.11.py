my_pizzas = ['pepperoni', 'meat lovers', 'cheese']
friend_pizzas = my_pizzas[:]

my_pizzas.append('super supreme')
friend_pizzas.append('hawaiian')

print("my favorite pizzas are:")
for pizza in my_pizzas:
    print(f"- {pizza}")

print("\nMy friend's favorite pizzas are:")
for pizza in friend_pizzas:
    print(f"- {pizza}")
