# Dunder mathods
# The underscores gotten below ar dunder methods.
# Dunder methods are special methods which allow us e python specific functions on objects created through our class.


class Toy():
    def __init__(self, color, age):
        self.color = color
        self.age = age
        self.my_dict = {
            'name': 'Yoyo',
            'has_pets': False
        }

    def __str__(self):
        return f'The color is {self.color}'

    def __len__(self):
        return 5

    def __call__(self):
        print('Yes?')

    def __getitem__(self, i):
        return self.my_dict[i]


# There are special cases to modify the dunder methods.
# And since __str__ was modified above, when called below it now returns red as well.
action_figure = Toy('red', 0)
print(action_figure.__str__())
# It's thesame as using,
print()
print(str(action_figure))  # This
# Str is only modified when we use it on a specific object which in this case is the 'action_figure' as a string above.(This)
print()
print(len(action_figure))
print()
print(action_figure())
print()
print(action_figure['name'])
# What's interesting to me is that even without writing the del action_figure
# ,it still shows it at the output.
