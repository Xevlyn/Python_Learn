# It is important to not that the values in the list are counted from 1 and not from 0!...Nope
# Read the documentation for these list methods.

basket = [1, 2, 3, 4, 5]
print(basket)
print()

# ADDING METHODS

### APPEND ###
new_list = basket.append(100)
print(new_list)

# The output is only shown when the basket is printed and not the new_list value
# This is because append changes the list in place meaning it doesn't produce a value and is just changing the list.
print()

### INSERT ###
basket.insert(5, 20)
#           index,value
print(basket)

# Insert just modifies the existing value in memory
# You can choose the index of the added value
print()

### EXTEND ###
basket.extend([2, 230, 222, 444])
print(basket)
print()
# Extend takes the iterable and it makes it to loop over
# Adds the new values according to the list which you input


# REMOVING METHODS
### POP ###

basket.pop()
print(basket)
print()
# Removes the last value from the list
# It can also be specific with the index you intend to remove

### REMOVE ###
basket.remove(4)
print(basket)
print()
# With remove() you must be specific with the index you intend to remove

### CLEAR ###
basket.clear()
print(basket)

# This wipes out everything in the list hence returning nothing
# It takes not arguments and working solely on the entire list at once
