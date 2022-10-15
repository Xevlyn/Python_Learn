# A set is an unordered collections of unique objects.
# Just like dictionaries but they have just values only.
# Sets just like dictionaries don't support indexing.
print()
my_set = {1,2,3,4,5,5}
# Keeping in mind that there's a duplicate in the set, 
# once the set is printed out each value remains unique
# ie knowing there are 2 5's, only 1 5 will be printed because it is a unique value in the set.
my_set.add(100)
print(my_set)
print()


# Return an array with no duplicates.
my_list = [1,2,3,4,5,5]
print(set(my_list)) #Here it's simply changing the datatype from list to set 

print()
# Verifying if a given value is within a set and checking the set length is possible.
my_set2 = {1,2,3,4,5,6,6}
print(1 in my_set2)
print()
print(len(my_set2))
print()
print(list(my_set2))
print()