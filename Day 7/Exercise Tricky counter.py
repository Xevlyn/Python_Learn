# Counter
mylist = [1,2,3,4,5,6,7,8,9,10]

counter = 0
# The counter is located out of the code block bcs
# , the variable its equated to remains constant and does not change
for item in mylist:
    # if counter = 0 was in the code block bcs
    # ,everytime a new count was being made with the variables within the list
    # ,it resets to 0 since its within the loop.
    counter = counter + item
    print(counter)
    # When the print counter is within the code block for the condition
    # ,It prints all of the values which have been added from the list
print()
print(counter)
# Where as when the output is printed out of the code block it prints out only the single output needed which is 55