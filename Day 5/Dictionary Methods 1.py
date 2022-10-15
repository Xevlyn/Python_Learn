user = {
    'basket': [1, 2, 3],
    'greet': 'Hello',
    'age': 20

}

print(user.get('age', 55))
# .get is a method which checks to see if there is a value in the dictionary
# the 55 value comes as a conditional output should it being that the key is not present in the dictionary.
print()

user_2 = dict(name='Matthew')
# the           key=value
print(user_2)
