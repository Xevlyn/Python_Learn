# This means hiding away of information and  giving access to only what's necessary.

class PlayerCharacter:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def run(self):
        print('run')

    def speak(self):
        print(f'my name is {self.name} and I am {self.age} old')
        # Encapsulated code in the string


print()
player1 = PlayerCharacter('Alex', 12)
player1.speak()
print()
print(player1.age)
# When the methods are taken off and player1 is printed, the player object is gotten but the name and the age can be accessed as well.
player1.name = '!!!'
player1.speak = 'BOOM!'
print(player1.speak)
print()
