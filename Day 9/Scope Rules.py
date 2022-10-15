a = 1
def parent():
    a = 14
    def confusion():
        return sum
    return confusion() # a is returned. 
# Confusion() runs as a separate function.

print(a)
print(parent())

# Both are printed out.
# This is because the function confusion() is  separate from the global variable a even though is in the confusion() function.

# Rules 
    # 1 Start with local variables
    # 2  if there's nothing in the local scope, is there a parent local scope?
    # 3- Global. Its the indentation of nothing
    # 4- Built-in python functions.