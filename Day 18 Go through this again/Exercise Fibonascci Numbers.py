# Create a function fib which takes a number and in (number), this number will be the index number of the fibonacci. This easier to do with generators bcs with a list it takes up a lot of resources.
def fib(number):
    a = 0
    b = 1
    for i in range(number):
        yield a
        temp = a  # a = 0
        a = b  # a = 1
        b = temp + b  # b = 0 + 1


for x in fib(21):
    print(x)
