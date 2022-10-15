# Tuples are like lists but unlike lists, you cannot modify them.
# Hence they are known as immutable lists
print()
my_tuple = (1, 2, 3, 4, 5)
print(5 in my_tuple)
print()

# Benefits of tuples
# Makes code more predictable
# Makes things easier and more efficient
# Makes code safer
# Faster than lists
# Example of use case location
#
# Downsides
# Makes code < flexible as compared to the lists ie you can not sort, reverse etc

user = {
    (1, 2): [2, 4, 6],  # Tuples are valid keys in dictionaries
    'basket': [1, 2, 3],
    'greet': 'Hello',
    'age': 20,
    (1, 2, 3, 4): 'Fighting'

}
print(user[(1, 2)])  # Returns the key:value as a tuple
print()
print(user[(1, 2, 3, 4)])
print()
print(user['age'])
print()
