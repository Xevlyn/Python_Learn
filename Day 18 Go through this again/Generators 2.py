# An iterable is any object in python which we're able to loop through underneath the hood having the dunder iter
# Generators are iterable but not everything that's  iterable is a generator.
# For example a range is a generator and will always be an iterable but a list is an iterable but not a generator.
#
# Hence generators are subsets of iterables..
# Difference btwn a generator and an iterable is the way we implement them.
# The generator

# Standard for of creating a generator function using the range and the yield keyword
def generator_function(num):
    for i in range(num):
        # Yield pauses the function gives  i and comes back later onto the generator
        yield i*2


g = generator_function(100)

next(g)
next(g)
print(next(g))
