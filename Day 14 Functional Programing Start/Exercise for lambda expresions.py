my_list = [5, 4, 3]
print()

# Create a one line lambda expression that will print a squared list meaning 5^2 = 25, etc.
print(list(map(lambda item: item ** 2, my_list)))

# List Sorting is the next challenge
# Sort the based on the list of tuples below from the lowest to the highest.
print()
a = [(0, 2), (4, 3), (9, 9), (10, -1)]
me = a.sort(key=lambda x: x[1])
print()
# From the key above it's programmed to run from the second item from each tuple in the given list.
print(a)
print()
print(me)
