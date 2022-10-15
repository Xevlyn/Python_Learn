list = [1,2,3]
for item in list:
    print(item)
print()

i = 0
while i < len(list):
    print(list[i])
    i += 1

    #While loops are more powerful than for loops
    # For loops are simpler than while loops.

# For simple loops for iterating over objects choose for loops
# Where as when u are unsure of the iterable objects choose the while loops.

while True:
    response = input('Say something: ')
    if (response == 'bye' ):
        break