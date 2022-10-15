def sum(num1, num2):
    return num1 + num2
print()
print(sum(4,5))
print()

# What the return function does is when placed in a certain function it exits the function and returns what ever the expression gives or modifies something.

# I'll eventually come back to this later on.
# But what you should know is it either returns something or modifies something

#Functions should do either of these things ie
    #Should do one thing really well
    #Should return something.

def add(ver1, ver2):
    print('hii')
    print()
    ver1 + ver2 
    # This will only print when return is placed at the front.
print()
print(add(4,5))
print()

# The above is an example not to follow. The function in the code is trying to do 2 things at thesame time and that can't work..hence just one thing is printed. Which is the hii and a none is returned.

yanky = sum(10,5)
print(sum(100,yanky))
# Since the function sum is in memory, when used in a diffrent scenario it does thesame as it did in the previous code which is add the 2 variables which have been defined already. which in this case is adding yanky with 100


def add1(vrs1, vrs2):
    def anth_fnc(vr1, vr2):
        return vr1 + vr2 # This is just defined but not runned  in the code  
    return anth_fnc(vrs1, vrs2) 
    # Gives the memory location of the function.
    # What is being used are the parameters called at the top.
print()
total = add1(17, 3)
print(total) # What is printed here is None

#To get the result of the function it's either 
    # The actual variables are given with the print(total)
    # or the variables are defined at the return anth_fnc(vr1,vr2)

# This function is not very good because it's confussing

# Return automatically exits the code
