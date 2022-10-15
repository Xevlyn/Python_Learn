print()
is_friend = True
is_User = False
# Short circuiting can be done when a condition like OR is used
# There's a difference in performance when it comes to the used of AND or OR bcs of short circuting
# When OR is used and the first condition is true, the 2nd condition is kinda ignored bu the interpreter
# bcs the 1st condition is already true and will be returned regardless.

# The AND condition however is used to actually confirm that both condition are true before returning the output of the program runned
# And when one of the conditions is false, then its short circuited to know what output to return..

if is_friend or is_User:
    print('Best friends forever!')
