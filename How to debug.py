# Debuging
# When debugging use the practice of linting allows use detect some issues when we write our code.
# We find errors before we write our code.
# An example of linting is the  case above where num is identified as an undefined value
# PDB, python debugger
# This debugger gives us the ability to interact with the code.
import pdb


def add(num1, num2):
    # pdb.set_trace()
    return num1 + num2


t = add(4, 5)
print(t)
# When runned it gives an interactive python debugger in the console which you can actually run and test the code which you write.
# Read through the pdb documentation for more information on what the commands do and how to use them.
