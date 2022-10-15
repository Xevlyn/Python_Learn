
# Map allows us simplify the code we have

my_list = [1, 2, 3]


def multiply_by2(item):
    #newlist = []
    # for item in li:
    #    newlist.append(item * 2)
    # return newlist

    # The above is replaced by this due to the presence of the map function.
    return item * 2


# Gives memory location of the map created from the object.
#print(map(multiply_by2, [1, 2, 3]))
print()
print(list(map(multiply_by2, my_list)))
# Map calls the function given to it at a given memrory address.
print(my_list)
print()
