# Clean Code is the idea of reducing the number of lines of code but coming up with the same output regardless.
print()
def is_even(ve):
    if ve % 2 == 0:
        return True
    elif ve % 2 != 0:
        return False
print(is_even(31))
print()


# Cleaned up
def is_even(xe):
    return xe % 2 == 0 # return True or false depending on if the conditions are met.    
    
print(is_even(32))
print()

# The elif is not really required bcs we are just checking for the evn value and not necessarily the odd value

# Also elif / else are not needed since the return function automatically exits the code after executing 

# Again given this specific condition, the if function is not required and the retrun function used solely ie the expression return ve % 2 == 0 checks if the value given is true or false by way of boolean expression as seen by the output given.