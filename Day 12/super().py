class User(object):
    def __init__(self, email):
        self.email = email

    # When the email is called from here for the user wizard
    # ,it shows that the email attribute is not part of the wizard.
    # But placing it within the Wizard attribute is inefficient since that too will be needed by other users.

    def sign_in(self):
        print('logged in')


class Wizard(User):
    def __init__(self, name, power, email):
        super().__init__(email)
        # This is calling the init method of the User inside the wizard.
        # This is one way of doing it
        # Another way is known as super which refers to the super class above wizard which is user and this is a new addition
        # suoer() needs no self
        self.name = name
        self.power = power

    def attack(self):
        print(f'Attacking with power{self.power}')


wizard1 = Wizard('Merlin', 56, 'merlin@gmail.com')
print(wizard1.sign_in())
print(wizard1.email)
