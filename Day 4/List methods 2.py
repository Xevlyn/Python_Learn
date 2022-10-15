# It is important to note that the values in the list are counted from 1 and not from 0!
# Read the documentation for these list methods.
# PART 2 Kinda thesame thing buh slightly different

# SEARCHING IN THE LIST
print()
basket = ['a', 'b', 'c', 'd', 'e']
#          0 , 1 , 2 , 3 , 4
print(basket.index('d', 2, 5))
print()
# This indicates the index positions of the given value in the list
# You can also give optional parameters to check within a given range in the list ie 'd',0,2
# This pinpoints to the EXACT POSITION OF A GIVEN INDEX
# Check to see the indexes underneath the list above
print('x' in basket)
print()
# From my understanding, it's like searching the list or any returned statement for a given value
# The output returns boolean values ie True or False to confirm if said value is in the index.

# COUNT
print(basket.count('a'))
# This is to determine how many times an item appears
