sandwich_orders = [
    'pastrami', 'tuna', 'pastrami', 'chicken', 
    'roast beef', 'pastrami', 'turkey'
]
finished_sandwiches = []

print("Sorry, the deli has run out of pastrami.\n")

while 'pastrami' in sandwich_orders:
    sandwich_orders.remove('pastrami')

while sandwich_orders:
    current_sandwich = sandwich_orders.pop()
    print(f"I made your {current_sandwich} sandwich.")
    finished_sandwiches.append(current_sandwich)

print("\n--- Finished Sandwiches ---")
for sandwich in finished_sandwiches:
    print(f"- {sandwich.title()} sandwich")