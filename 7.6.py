# Use a conditional test in the while statement to stop the loop
prompt = "\nEnter a pizza topping (type 'quit' to finish): "
topping = ""

while topping != 'quit':
    topping = input(prompt)
    if topping != 'quit':
        print(f"I'll add {topping} to your pizza!")


# Use an active variable to control how long the loop runs
prompt = "\nEnter a pizza topping (type 'quit' to finish): "
active = True

while active:
    topping = input(prompt)
    if topping == 'quit':
        active = False
    else:
        print(f"I'll add {topping} to your pizza!")


# Use a break statement to exit the loop when the user enters a 'quit' value
prompt = "\nEnter a pizza topping (type 'quit' to finish): "

while True:
    topping = input(prompt)
    if topping == 'quit':
        break
    print(f"I'll add {topping} to your pizza!")