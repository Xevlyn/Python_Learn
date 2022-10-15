# A pure function has 2 rules..
# #Given the same input it will always give the same output.
# #A function should not produce any side effects.

#
def multiply_by2(li):
    newlist = []
    # Second a=rule applied since this is within the function and not outside.
    for item in li:
        newlist.append(item * 2)
    return newlist


# First rule applied.
print(multiply_by2([1, 2, 3]))
