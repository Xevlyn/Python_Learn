# Inheritance allows new objects take on the properties of existing objects.

# Users here can have multiple forms from Wizards to archers but they'll have to be signed in first.
# The class of each character must have access to the sign_in class under user.
class User:
    def sign_in(self):
        # The __init__ method is option and can be placed depending on the code condition.
        print('logged in')

# In order to do this -what is said above- you make sure to pass the paren class to the current class you are working with.


class Wizard(User):
    def __init__(self, name, power):
        self.name = name
        self.power = power

    def attack(self):
        print(f'Attacking with power of {self.power}')


class Archer(User):
    def __init__(self, name, arrows):
        self.name = name
        self.arrows = arrows

    def attack(self):
        print(f'Attacking with arrows : arrows left - {self.arrows}')


wizard1 = Wizard('Merlin', 50)
archer1 = Archer('Robin', 100)
# Th functionality has been inherited from the parent class above it.
wizard1.attack()
print()
archer1.attack()
