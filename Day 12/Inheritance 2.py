# Inheritance 2
# The tool used to check if something is an instance is isinstance
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
print(isinstance(wizard1, object))
# isinstance(instance, class) to be checked

# The output here is True bcs wizard1 is an instance of Wizard

# The output here is also True bcs wizard1 is an instance of User bcs we've had to run the class to get wizard1.

# The output here is also True bcs wizard1 inherits or gets methods from the object class as well as the wizard and the user classes .
# In python everthing inherits from the base object class python comes with. Hence why you see all those dunder methods at the side.
