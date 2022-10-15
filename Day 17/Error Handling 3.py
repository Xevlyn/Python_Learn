# When you want to write in your own error message when the case is very serious and can't be ignored
while True:
    try:
        age = int(input('what is your age? '))
        10/age
        raise ValueError('Hey! Cut it out')
    except ZeroDivisionError:
        print('PLease enter a number higher than 0')
    else:
        print('Thank you')
    finally:
        print('Okay! . Finally I\'m done!')
    print('Can you hear me? ')
