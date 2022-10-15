# What is encapsulation?
# It is the binding of data and functions that manipulate that data and this is done to keep everything in this one box which are able to interact with other boxes in the  code.

class PlayerCharacter:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    # def run(self):
    #    print('run')

    # def speak(self):
    #    print(f'my name is {self.name} and I am {self.age} old')
    #    # Encapsulated code in the string


print()
player1 = PlayerCharacter('Alex', 12)
# player1.speak()
print(player1.age)
# When the methods are taken off and player1 is printed, the player object is gotten but the name and the age can be accessed as well.
print()

player2 = {'name': 'Micheal', 'age': 14}
print(player2['name'])
# In order to access the keys in the dictionary for player2, we call them by using a list.
print()
print(player2['age'])
