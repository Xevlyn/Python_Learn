# OOP gives us a way to create our own methods such as run and attributes like self.name
# OOP allows us to write code that is repeatable, well organized nad also memory efficient cuz the code is written just once.

class PlayerCharacter:
    membership = True
    # Class object attributes aren't dynamic but static
    # This exists for all objects inside this class ie True/False for all within this class depending on the condition used.
    # it has to be singular since its a blue print

    def __init__(self, name, age):
        # self is like the this keyword in javascript and other languages.
        if (PlayerCharacter.membership):
            self.name = name  # Attributes which the objects have.
            self.age = age

    def run(self):
        print(f'my name is {self.name}')
        return ''

    def shout(self):  # Method
        print(f'my name is {self.name}')
        return ''
        # Class object attributes don't change across classes.
        # Where as an attribute or a class attribute is dynamic and specific to each class object.
        # Hence in order to be able to access a name or age you must use the self. attribute.


player1 = PlayerCharacter('Sammy', 21)
# player1 is the object/variable
player2 = PlayerCharacter('Jacky', 35)
player2.attack = 45

print(player1.run())
print(player2.shout())
# help(player1)  # gives a blueprint of a given object
