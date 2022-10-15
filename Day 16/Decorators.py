# What are decorators
# example @classmethod

# Functions in python are first class citizens in python and this is the whole concept of decorators.
def hello(func):
    func()


def greet():
    print('still here!')


a = hello(greet)

print(a)


# Decorators suppercharge our function
