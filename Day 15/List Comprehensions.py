# Unique to the python programing language.
# Alternatively they're called list/set/dictionary comprehensions.

# Comprehensions are simply quick ways of creating list or sets or dictionaries instead of looping or appending in diffrent lists.
my_list = []
print()
for char in 'hello':
    my_list.append(char)

print(my_list)

print()
# Now with list comprehensions
my_list2 = [xter for xter in 'Hello there!']
#           param for param in iterable
# Basically from what I understand is
# There's a loop within the list which is clearly visible and the items for a given parameter of an iterable are printed.
#
# If confused in the future come and re-watch the video
print(my_list2)
print()

# To print a list of numbers
my_list3 = [num for num in range(10)]
# To multiply the range of numbers

my_list4 = [num * 2 for num in range(0, 10)]

# To get the even numbers

my_list5 = [num ** 2 for num in range(10) if num % 2 == 0]
print(my_list3)
print()
print(my_list4)
print()
print(my_list5)
print()
