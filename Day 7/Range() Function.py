# Range is a function that returns an object which produces a sequence of integers 
# from start (inclusive) to stop (exclusive) by step.
print()
print(range(100))
print()

for number in range(0, 10):
    print(number)
print()   

for emails in range(0, 10):
    print('Congratulations! ')
print()

for _ in range(0, 10 , 2):
    #         range, step over
    print(_)
    # Used when the only interest is for the range() function and no the variable
print()

for countdown in range (10, 0, -2):
    #               range in reverse, reverse
    # 10, 0 won't work
    print(countdown)
print() 

for _ in range(2): # This loops 2wice
    print(list(range(10)))
    # This prints a list of 10
    # It can also work with other datatypes such as tuples.
print