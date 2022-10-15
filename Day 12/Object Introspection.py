# Introspection refers to the ability to determine the type of object at runtime.
# ie when the code is running.
# so practically examining the code when running.

class User(object):
    def __init__(self, email):
        self.email = email

    def sign_in(self):
        print('logged in')


class Wizard(User):
    def __init__(self, name, power, email):
        super().__init__(email)
        self.name = name
        self.power = power

    def attack(self):
        print(f'Attacking with power{self.power}')


# Down here
wizard1 = Wizard('Merlin', 56, 'merlin@gmail.com')
# dir gives all the methods and attributes wizard has access to.
print(dir(wizard1))
