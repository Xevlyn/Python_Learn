# Lambda Expressions
# These are one time anonymous functions that you don't need more than once
# MEANING they are useful when using them for functions that need
#   You only need once
#   There are anonymous functions.
from functools import reduce

# lambda param: action(param)
#    lambda item: item*2
my_list = [1, 2, 3, 4, 5, 6, 7]

# Example when you want to use the following function just once and discard of it
# The function below has been commented out but when we run it in the print function below, it functions as the multiply_by2 function but only once.

# def multiply_by2(item):
# return item * 2


# def check_odd(item):
#    return item % 2 != 0


# def accumulator(acc, item):
# return acc + item

# Advantages of Lambda Expressions:
# They make the code look clean and small
# Good for running one time processes.

# Disadvantages of Lambda Expressions:
# The code looks less readable to some programers who look at your code.


print()

print(list(filter(lambda item: item % 2 != 0, my_list)))  # Odd numbers.
print()
print(list(filter(lambda item: item % 2 == 0, my_list)))  # Even numbers.
print()
print(reduce(lambda acc, item: acc + item, my_list, 2))  # reduce
print()
print(my_list)
