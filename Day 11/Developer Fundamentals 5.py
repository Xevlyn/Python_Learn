# Test Your assumptions
# When ever u are thought something new either by a book or some video, u test it in a certain condition or conditions to get the output an compare what was said about it with the output.

# Test fro the self kwrd
class PlayerCharacter:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def run(self):
        return self


player1 = PlayerCharacter('Xevlyn', 21)

print(player1.run())
