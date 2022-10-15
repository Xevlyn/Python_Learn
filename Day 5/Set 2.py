# Methods for set datatype
# .difference() method
# .discard() method
# .difference_update() method
# .intersection() method
# .isdisjoint() method
# .issubset() method
# .issuperset() method
# .union() method 

my_set = {1,2,3,4,5}
your_set = {4,5,6,7,8,9,10}
uni_set = {7,8,9}
## Difference Method ##
print()
print(my_set.difference(your_set))
print()
print(your_set.difference(my_set))
print()
# What this does is print out the differences btwn the 2 sets 
# Meaning what is my_set that isn't in your_set ie {1,2,3}
# and what is in your_set that isn't in my_set ie {6,7,8,9,10}

## .discard() method ##
# my_set.discard(5)
# print(my_set)
print()
# Removes the desired value from the set specified

## .difference_update() method ##
# my_set.difference_update(your_set)
# print(my_set)
# print()
# This removes the differences ie 4,5


# .intersection() method
print(my_set.intersection(your_set))
print()
print(my_set & your_set) # Shorter method for intersection
print()
# Returns the values which interset the 2 sets ie 4,5


## .isdisjoint() method ##
print(my_set.isdisjoint(your_set))
print()
# is disjointed means do the sets involved have nothing in common hence for this case the retrun value here will be FALSE since the sets involved have 4,5 in common

## .union() method  ##
print(my_set.union(your_set))
print()
print(my_set | your_set) # Shorter method for union
print()
# union unites both sets 2gether returning a new set making sure not to include duplicates.

## .issubset() method ##

print(uni_set.issubset(your_set))
print()
# Its in the name but this just means are the values in uni_set found in your_set which is TRUE


## .issuperset() method ##
print(uni_set.issuperset(your_set))
print()
# Meaning does uni_set encompass your_set which is FALSE
