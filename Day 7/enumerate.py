# enumerate
# Returns an enumerate object and iterable must be another object that supports iteration
# it takes an iterable object and gives an index counter and the item of that index.
print()
for i,char in enumerate('Hello'):
    print(i, char)
    # Returns the index of each item in the string
print()

for i,char in enumerate(list(range(100))):
    if char == 50:
        print(f'The index of 50 is:  {i}')