# Error handling allows us to let the script keep running even when there's an error
# In error handling the use of the try block is key where by:
# if what is required by the code isn't entered then an alternative rather than an error is displayed.
while True:
    try:
        age = int(input('what is your age? '))
        print(age)
    except:
        print('PLease enter a number')
    else:
        print('Thank you')
        break

# The loop is there to ensure that the value is if what  is required isn't entered, the user must include it before moving on.
# The try, except, else block is used in error handling
# For each level of the block you can also decide on what specific error its, handling.


while True:
    try:
        age = int(input('what is your age? '))
        10/age
        print(age)
    except ValueError:
        print('PLease enter a number')
    except ZeroDivisionError:
        print('PLease enter a number higher than 0')
    else:
        print('Thank you')
        break
