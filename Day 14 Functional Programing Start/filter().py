# Filter: Filters things as in the name it has.
# We can sometimes receive less than what was given to it.

# Basically, we create various functions which we then use to get any desired outcome ie if we're searching for the odd value or the even value etc
my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]


def multiply_by2(item):
    return item * 2


def check_odd(item):
    return item % 2 != 0


def check_even(item):
    return item % 2 == 0


print()
#print(list(map(multiply_by2, my_list)))
# print()
print(list(filter(check_odd, my_list)))
print()
print(list(filter(check_even, my_list)))
print()
