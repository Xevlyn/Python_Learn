# Polymorphism is a pillar which means many forms.\

# And in python, it refers to the way that object classes can share thesame method name but those names can act differently based on what the objects where called for.

class User:
    def sign_in(self):
        # The __init__ method is option and can be placed depending on the code condition.
        print('logged in')

    def attack(self):
        print('Do something')

# In order to do this -what is said above- you make sure to pass the parent class to the current class you are working with.

# Polymorph example here is attack which are thesame but act differently based on their attributes.


class Wizard(User):
    def __init__(self, name, power):
        self.name = name
        self.power = power

    def attack(self):
        User.attack(self)
        print(f'Attacking with power of {self.power}')


class Archer(User):
    def __init__(self, name, arrows):
        self.name = name
        self.arrows = arrows

    def attack(self):
        print(f'Attacking with arrows : arrows left - {self.arrows}')


wizard1 = Wizard('Merlin', 50)
archer1 = Archer('Robin', 1000)
print(wizard1.attack())

# Polymorph
#
# 1
# for char in [wizard1, archer1]:
#    char.attack()

# 2
# def player_attack(char):
#  char.attack()

# player_attack(wizard1)
# player_attack(archer1)
