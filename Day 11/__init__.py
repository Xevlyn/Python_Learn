class PlayerCharacter:
    membership = True

    def __init__(self, name='Anonymous', age=0):
        if (age > 18):
            self.name = name  # Attributes which the objects have.
            self.age = age

    def shout(self):
        print(f'my name is {self.name}')


player1 = PlayerCharacter('Sammy', 21)

print(player1.shout())
