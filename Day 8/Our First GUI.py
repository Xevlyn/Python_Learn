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

for image in picture:
    for pixel in image:
        if (pixel == 1):
            print('*', end=' ')
        else:
            print(' ', end=' ')
    print(' ') # Required for the actual tree structure to come out.
