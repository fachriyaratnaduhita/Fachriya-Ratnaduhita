from random import randint

class Die:
    """A class representing a physical die."""

    def __init__(self, sides=6):
        self.sides = sides

    def roll_die(self):
        """Return a random number between 1 and the number of sides."""
        return randint(1, self.sides)

# Membuat dadu 6 sisi dan lempar 10 kali
print("Rolling a 6-sided die 10 times:")
d6 = Die()
results_6 = [d6.roll_die() for _ in range(10)]
print(results_6)

# Membuat dadu 10 sisi dan lempar 10 kali
print("\nRolling a 10-sided die 10 times:")
d10 = Die(sides=10)
results_10 = [d10.roll_die() for _ in range(10)]
print(results_10)

# Membuat dadu 20 sisi dan lempar 10 kali
print("\nRolling a 20-sided die 10 times:")
d20 = Die(sides=20)
results_20 = [d20.roll_die() for _ in range(10)]
print(results_20)