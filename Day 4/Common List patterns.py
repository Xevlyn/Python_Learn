print()

basket = ['a','b','d','c','d','e','f','x']
print()

basket.sort()
basket.reverse()
print(basket)
print()

# Output ['f','e','d','d','c','b','a']

# Another method of reversing
print(basket[::-1])
# This is list slicing
# This creates an entirely different list from the original which is unsorted.
print()
print(basket)

### RANGE LISTS ###

print()
print(list(range(100)))
#  Generates a list or values from start to stop of the input which is provided ie if 1,100 it will print out numbers from 1 to 100 
# 
#  Output here is 1 to 99 for 1, 100
#  Output for 100 only is 0 to 99
#  Note that if not wrapped in a list, it will actually print out print(range(1,100))
print()

### JOINED ###

# Something that works on strings ie string method name

sentense = ' g '
mark_up = sentense.join(['hi','my','name','is','jojo'])
# For this method the join functions according to the value placed before it
# meaning if 'g' was found as the attached value to sentense, that's what will be used to join the sentense together.
print(mark_up)
print()

# Shorter way of doing it.
sentense = ' j '.join(['hi','my','name','is','jojo'])
print(sentense)
# which in this case ' j ' is the joiner



print()