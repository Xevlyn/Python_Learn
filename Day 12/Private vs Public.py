# Private Variable Creation
# An example of a language which does this is java

class PlayerCharacter:
    def __init__(self, name, age):
        # Dunder methods

        # This is a convension which indicates the variable is private ie the underscore
        # So when ever you see it is private and SHOULDN'T BE TOUCHED!
        # Note that its just a convension so
        self._name = name
        self._age = age

    def run(self):
        print('run')

    def speak(self):
        print(f'my name is {self.name} and I am {self.age} old')
        # Encapsulated code in the string


print()
player1 = PlayerCharacter('Alex', 12)
player1.name = '!!!'
player1.speak = 'BOOM!'
print(player1.speak)
print()
