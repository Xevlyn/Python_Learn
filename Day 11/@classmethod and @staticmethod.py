class PlayerCharacter:
    membership = True

    def __init__(self, name, age):
        if (age > 18):
            self.name = name  # Attributes which the objects have.
            self.age = age

    def shout(self):
        print(f'my name is {self.name}')

    @classmethod
    # This method can be used without instantiating a class.
    # This method is rearely needed.
    def adding_things(cls, num1, num2):
        # this parameter is the class
        return cls('Teddy', num1 + num2)

    @staticmethod
    def adding_things2(num1, num2):
        return num1 + num2

# player1 = PlayerCharacter('Sammy', 21)


player3 = PlayerCharacter.adding_things(2, 3)

print(player3.age)
