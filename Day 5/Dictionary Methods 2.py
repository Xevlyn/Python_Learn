print()
user = {

    'basket': [1, 2, 3],
    'greet': 'Hello',
    'age': 20

}

print('Hello' in user.values())
print()
print('age' in user.keys())
print()

#   the .keys() and .values() methods are used as a means of validating if truly a value is found within the dictionary.
#   these return specifically the booleans for the keys and values method.
print(user.items())
print()
# OUTPUT dict_items([('basket', [1, 2, 3]), ('greet', 'Hello'), ('age', 20)])
# Gives tuples within a list

# Clear #

# print(user.clear())
# print()
# The output here just returns an empty value
# user.clear()
# print(user)
# print()
# .clear creates an empty dictionary

##user2 = user.copy()
# print(user2)
# An actually copy is made but assigned to a separate value
# print(user.pop('age'))
#   Returns then Removes a key and  value from the dictionary
# print(user)
# print()
# This prints the value users which is the original at the top

# print(user.popitem())
# print()
# print(user)
print()
# It randomly removes a key and value in the dictionary
# In this case it removes the last item on the dictionary.
# But if this was a massive dictionary, keep in mind that dictionaries are unordered hence the item popped off may be random.

## Update ##
# As in the name it updates a key:value pair in the  dictionary
print(user.update({'greet': 'Bonjour!'}))

# If the key place is not in the list, It will be printed in the output as the last value hence leaving the previous key value pair untouched.
print()
print(user)
