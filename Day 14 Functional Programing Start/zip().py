# Works like a zipper to zip two lists together.
# Filter: Filters things as in the name it has.
# We can sometimes receive less than what was given to it.
my_list = [1, 2, 3, 4, 5, 6, 7, 8]
ur_list = [11, 12, 13, 14, 15, 16, 17, 18]
their_list = [19, 20, 21, 22, 23, 24, 25, 26]


print()
#print(list(map(multiply_by2, my_list)))
# print()
print(list(zip(ur_list, my_list, their_list)))
print()
# Zip grabs the first items of each ie 1 and 11 and are added together as a tuple and prints them in a list, []
# It doesn't matter if the information is within a tuple itself it will still be printed as a tuple.
# Even if they're 3 list the first of each are placed together in a tuple and then teh others follow suit.
