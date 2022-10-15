# An iterable is simply an object or collection which can be iterated over
# It can be a list, tuple, dictionary, set, string
# iterated is the action of one by one check of each item in the collection.

print()
user = {
    'name': 'Golem',
    'age': 5006,
    'can_swim': False
}

for positions in user:
    print(positions)
print()
# Any word can be used to describe the key value pairs within the dictionary.
# This returns the key pairs.

print()
for positions in user.items():  # .items() method
    print(positions)
print()

for positions in user.keys():  # .keys() method
    print(positions)
print()

for positions in user.values():  # .values() method
    print(positions)
print()

for key, value in user.items():  # .items() method Alternative
    # Directly above can be any value
    # Keys and values are not printed as tuples with this method.
    print(key, value)
print()
