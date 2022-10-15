# Re-watch this
# Main idea is writting code which can be implemented everywhere in the code when called.

class PlayerCharacter:
    # it has to be singular since its a blue print
    def __init__(self, name, age):
        # the __init__ method is a special method used in a class. It's also kwn as a constructor method.
        # called automatically anytime we instantiate.
        # Instantiate means calling the class to create an object.
        self.name = name  # Attributes which the objects have.
        self.age = age

        # the self kywrd is a way to define the PlayerCharacter created like player 1.
        # Removing the self gives the output as 'object has no attribute name' bcs to make the player have a name u must have self cuz it refers to player 1

    def run(self):
        print('run')
        return 'Fun.'


player1 = PlayerCharacter('Sammy', 21)
player2 = PlayerCharacter('Jacky', 35)

print(player1.run())
print(player1.age)
print()
print(player2.name)
print(player2.age)
print()
print(player1)  # Gives memory locations of the diffrent players
print(player2)
