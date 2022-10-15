# reduce()
# Reduce doesn't come as part of the built in function.
# It should be imported

# From functional tools import the reduce() function.
from functools import reduce
my_list = [1, 2, 3, 4, 5, 6, 7]


def multiply_by2(item):
    return item * 2


def check_odd(item):
    return item % 2 != 0


def accumulator(acc, item):
    # The accumulator, acc here is the initial while the item is the sequence.
    # Takes 2 parameters called by reduce.
    #
    # Accumulator will equal 0 when it hasn't been given a value yet.
    print(acc, item)
    return acc + item


print()
#print(list(map(multiply_by2, my_list)))
#
print(reduce(accumulator, my_list))
# Reduce allows use reduce something from the variable
# The list is removed because the reduce() function places a list
print()
print(my_list)
