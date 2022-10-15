# Higher order functions can be one of two things:
# It ca either be a function that accepts another function as a parameter.
def greet(func):
    func()

# or
# Its a function that returns another function.


def greet2():
    def func():
        return 5
    return func

# maps(),filter(),reduce() are higher order functions.


print(greet2())
