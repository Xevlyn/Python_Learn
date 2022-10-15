# How to organize code together from separates python files.
# Modules are .py files which have been linked up together and function together.
# Its similar to classes and  functions.
# Case study is Netflix where there are separate modules for videos and subscriptions etc

# We use the import command to communicate btwn the two files
# import packages.shopping.moreshopping.shopping_cart
# There's an easier way of doing this below
# Still works and  its cleaner
# from modules import mult, divide rather than doing this, you can do the following
# bcs * is a wildcard which means all the values of that given folder.
from modules import *


from packages.shopping.moreshopping import shopping_cart
# You can equally import a package folder but don't forget to write it in the print.
# Reason is sometimes there are name collisions
if __name__ == '__main__':
    print(mult(5, 2))
    print()
    print(divide(10, 2))
    print()
    print(shopping_cart.buy('apples'))
    print()
    print('Please Run this!')

# A pycahe is created when ever we are creating modules from separate files
# This means that anything that's been imported from the modules folders is cached in the pycache folder.
# We don't touch the pycache folder .

# Next video  __name__
# WHat is the __name__ and what does it do?
# Used because there are time when we wish to run specific folders within our python codes knowing that's the main folder/file being executed.
