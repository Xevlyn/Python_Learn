# Decorators supercharges are function ie function that wraps another function and enhances or changes it
def hello():
    print('Hello')


def my_decorator(func):
    def wrap_func():
        print('*********')
        func()
        print('********')
    return wrap_func


@my_decorator
def hello():
    print('Hello')


@my_decorator
def bye():
    print('see you later')


hello()
bye()


# This can equally be runned as followes:
# It wraps the hello function and returns it
print()
my_decorator(bye)()
