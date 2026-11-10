from random import choice

def get_random_ticket(possibilities):
    """Generate a random 4-item ticket."""
    ticket = []
    while len(ticket) < 4:
        pulled_item = choice(possibilities)
        if pulled_item not in ticket:
            ticket.append(pulled_item)
    return ticket

# Kemungkinan elemen undian
possibilities = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 'a', 'b', 'c', 'd', 'e']

# Tiket andalan Anda
my_ticket = [5, 9, 'a', 'c']

plays = 0
won = False

# Looping sampai tiket Anda cocok dengan hasil undian
while not won:
    new_ticket = get_random_ticket(possibilities)
    plays += 1
    
    # Membandingkan tiket tanpa memperdulikan urutannya
    if sorted(new_ticket, key=str) == sorted(my_ticket, key=str):
        won = True

print(f"It took {plays} tries to win the lottery with ticket {my_ticket}!")