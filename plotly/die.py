from random import randint

class Die:
    # A class representing a single class.

    def __init__(self, num_sides = 6):
        # Assume a six side die.
        self.num_sides = num_sides

    def roll(self):
        # Return the random value between 1 to number of sides.
        return randint(1, self.num_sides)