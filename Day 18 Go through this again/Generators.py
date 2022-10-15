# A generator allow us generate a sequence of values overtime
# Examples include range(),
range(100)


def make_list(num):
    result = []
    for i in range(num):
        result.append(i*2)
    return result


# Points to a location in memory and takes up space in it
my_list = make_list(100)
print(list(range(10000)))


# Watch generators again
