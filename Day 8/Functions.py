# Function examples were print , input etc
# It is also possible of creating ur own function
print()
def say_hello(): 
    # def is used to define the function we want to use
    print("Hello") # Its been created but in order to use the function, it has to be called before it prints.
say_hello()
print()

# functions as used when u have to repeat certain  lines of code.


# in order to run this code multiple times without actually copying it again.


picture = [

    [0,0,0,1,0,0,0],
    [0,0,1,1,1,0,0],
    [0,1,1,1,1,1,0],
    [1,1,1,1,1,1,1],
    [0,0,0,1,0,0,0],
    [0,0,0,1,0,0,0]

]
print()


def show_tree():
    fill =  "*"
    empty = ' '
    for image in picture:
        for pixel in image:
            if (pixel): # Removed ==1 since pixel is a truthy value hence recognized automatically as 1
                print(fill, end=' ')
            else:
                print(empty, end=' ')
        print(' ')

show_tree()
# Since the show_tree function has been defined , it prints out the trees in relation to the number of functions written in the
# Once the show tree is written before the line it has been defined on, it won't print out because the interpreter moves line by line and the line which its been defined on appears after.
# Hence an error message is printed
print()
print(show_tree) 
    # This shows the location/bookshelve where the show_tree has been saved on 