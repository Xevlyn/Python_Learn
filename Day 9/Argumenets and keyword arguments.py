# What are they? - Although we've seen something on that before though.

# Arguments - *args
# Keyword arguments - *kwargs

def super_func(*args, **kwargs):
    # By including the star in front of the args, it indicates that any amount of arguments are accepted not just 1 argument. (*args)

    total = 0
    # With the kwargs as in the name , keywords can be added.. 
    print(*args)
    print()
    for items in kwargs.values():
        total += items
    print()
    # \*args gives all the arguments 
    # Where as when the its args its gotten as a topple
    return sum(args) + total
print(super_func(1,2,3,4,5, num1=5, num2=10))

print()

    # \*args allow us to grab the positional arguments below and just sum them up and return
    # \*kwargs allow us to grab  any amount of keyword arguments and get a dictionary which comes as keyword args and use them as we please in lopping fro this case

#RULE FOR ORDERING
    #params, *args, default parameters, **kwargs
    # Meaning the parameters come before the *args and default parameters b4 the **kwargs

    #eg def super_func(name, *args, i='hi', **kwargs):
    