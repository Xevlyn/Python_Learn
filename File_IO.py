# File I/O which stands for input output
# I/O simply means inputing something from the outside world and outputting to the output world.
# pythons built in file named opened allows us to open and write to files and it is callled open
my_file = open('touch.txt')
print()
print(my_file.read())
print(my_file.readline())

my_file.close()
# Only the first is printed and the others ignored because you can only read the file once due to the idea of a cursor.
# The way we get past this is by the use of the seek ie my_file.seek(0)
# You have to manually close the f iel after you have used it. This is done bcs its a good standard.
