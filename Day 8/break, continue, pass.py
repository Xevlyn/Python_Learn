my_list= [1,2,3]
print()

for item in my_list:
    #print(item)
    #continue
    pass

print()

i = 0
while i < len(my_list):
    print(my_list[i]) # Prints the actual elements in my_list and not the indexes.
    i += 1
    pass
print()

# With break statement breaks out of the current enclosing loop ie if 1 was looped first, it'll be printed and the code stops running.
# With continue statement when one output is printed, the code keeps running until the last value is printed from the list, tuple or dictionary.
# Pass doesn't do anything but it's a good way to have a placeholder in the code.
    # I understand pass as when you intend to write some line of code but not in the current moment
    # .so you place pass in order to continue to the next line of code without interupting.