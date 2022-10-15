# Scope means what variables do I have access to?
# Scope is like a new world were by anything which is indented inside is its own world 

# total = 100 
# Global scope meaning everyone on this file has access to this variable.
# Everytime a variable is created and is not inside the function it is part of the global scope
if True:
    x = 10

def somefunc():
    just = 100
    return just
print(x)
print(somefunc())