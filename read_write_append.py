# Built-in with statement
# With the use of the with statement, you don't have to worry about the use of the close statement
with open('touch.txt', mode='a') as my_file:
    print()
    text = (my_file.write(':)'))
    print()
    print(text)
# Mode = 'r' specifies for reading
# Mode = 'w' specifies for writing
# Mode = 'a' specifies for appending
