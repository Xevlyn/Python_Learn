# Decorator Pattern
# It is called a  decorator pattern reason being that it give the decorator flexibility in order for us to pass any arguments into the function and then unpacking them in a function
def my_decorator(func):
    def wrap_func(*args, **kwargs):
        # *args and **kwargs are for the positional and keyword arguments
        print('*********')
        func(*args, **kwargs)
        print('********')
    return wrap_func


@my_decorator
def hello(greeting, emoji=':('):
    print(greeting, emoji)


hello('Hey')
