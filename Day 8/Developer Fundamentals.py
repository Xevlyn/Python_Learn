# What is good code ?
    # Clean 
    # Are we following the best practices ?
    # Readability. Is the code easy to understand by diffrent programmers ?
    # Predictability.. Can you predict what will happen next
    # DRY.. Don't repeat yourself

print()
picture = [

    [0,0,0,1,0,0,0],
    [0,0,1,1,1,0,0],
    [0,1,1,1,1,1,0],
    [1,1,1,1,1,1,1],
    [0,0,0,1,0,0,0],
    [0,0,0,1,0,0,0]

]
print()
# Steps
#  1 iterates over picture
# if 0 = print ' ' 
# if 1 = print *
fill =  "*"
empty = ' '
for image in picture:
    for pixel in image:
        if (pixel): # Removed ==1 since pixel is a truthy value hence recognized automatically as 1
            print(fill, end=' ')
        else:
            print(empty, end=' ')
    print(' ')
