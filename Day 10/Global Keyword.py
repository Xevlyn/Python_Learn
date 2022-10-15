yank = 0
def count():
    global yank 
    # The global keyword is a way of gaining access to the yank variable outside this function.
    yank += 1
    return yank

print(count())
print()

# There's a better way to do this known as dependency injection - the idea is to  do the following:

yanky = 0
def count(yanky):
    # global yanky 
    # The global keyword is a way of gaining access to the yank variable outside this function.
    yanky += 1
    return yanky

print(count(count(count(yanky)))) # Count done 3 times

# Here the dependency of the count function on yanky from the outside global scope is detached and focus on its health.
