guest_dinner = ['Budi', 'Rani', 'Cinta', 'Ana', 'Ika', 'Dian']
print("Sorry, the new table didn't arrive on time, I can only invite two people")

popped_guest = guest_dinner.pop()
print(f"Sorry {popped_guest}, I can't invite you to dinner.")

popped_guest = guest_dinner.pop()
print(f"Sorry {popped_guest}, I can't invite you to dinner.")

popped_guest = guest_dinner.pop()
print(f"Sorry {popped_guest}, I can't invite you to dinner.")

popped_guest = guest_dinner.pop()
print(f"Sorry {popped_guest}, I can't invite you to dinner.")

print(f"{guest_dinner[0]}, you're still invited to my dinner party")
print(f"{guest_dinner[1]}, you're still invited to my dinner party")

#menghapus 2 nama terakhir
del guest_dinner[0]
del guest_dinner[0]
print(guest_dinner)