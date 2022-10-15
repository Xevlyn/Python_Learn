# A parameter
# Arguments are used as the actual values we provide to a function


# Positional arguments are arguments that are required to be in the proper position. ie if when the parameters where defined as name , emoji the arguments must be in that order to be properly returned.

# Keyword arguments makes it possible for us not to worry  about the position.
def show_tree(name, emoji):
    #           variable/parameters
    print(f'Hello {name} {emoji}')
    # The parameters created above can be used in the print
print()

# These are positional arguments
show_tree('Jacob', '😃') # These are the arguments
show_tree('Fritz', '😃')
show_tree('Jack', '😃')
show_tree('Anna', '😃')
# Parameters are used for when we define the function
# Arguments are used for when we we call / invoke the function

# Keyword arguments
# This is bad practice cuz it complicates the code more than how it actually is
show_tree(emoji='😀', name='Emiley')

#Keyword arguments are confused with default parameters

#Default parameters allow us to give what we want as default where we define the function at once.
# When you're unable to call functions which have been given, print out the default names given as shown below.

# In my opinion this is the best followed by the positional arguments
def mantel(name='Kendrick', emoji='😠'):
    print(f'Hey {name} {emoji}')
print()

mantel()
mantel('Fred', '😃')