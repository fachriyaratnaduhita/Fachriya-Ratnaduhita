guest_dinner = ['Tina', 'Ana', 'Ika']
cant_dinner = guest_dinner[0]
print(cant_dinner)

#Mengganti tamu yang tidak bisa hadir
guest_dinner[0] = 'Rani'

#Pesan untuk setiap tamu setelah pergantian tamu
message = f"Hello {guest_dinner[0]}, I'm inviting you to my dinner event tonight."
print(message)

message = f"Hello {guest_dinner[1]}, I'm inviting you to my dinner event tonight."
print(message)

message = f"Hello {guest_dinner[2]}, I'm inviting you to my dinner event tonight."
print(message)

