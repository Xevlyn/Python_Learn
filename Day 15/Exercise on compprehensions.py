from multiprocessing.reduction import duplicate


# Finding the duplicates in a list of duplicates nad returned them in a list
some_list = ['a', 'b', 'c', 'b', 'd', 'm', 'n', 'n']

duplicates = []
for value in some_list:
    if some_list.count(value) > 1:
        if value not in duplicates:
            duplicates.append(value)

print(duplicates)

# Printing in one line of code using comprehensions to get the duplicates in some_list

Double = list(set([v for v in some_list if some_list.count(v) > 1]))
print()
print(Double)
