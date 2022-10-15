while True:
    try:
        age = int(input('what is your age? '))
        10/age
        print(age)
    except ValueError:
        print('PLease enter a number')
        # This cause send is back to the top when a wrong value has been added.
        continue
    except ZeroDivisionError:
        print('PLease enter a number higher than 0')
        # break  # R1
    else:
        print('Thank you')
        # break  # R2
    finally:  # This runs regardless if you've given the wrong information just for recording a sessions in activities such as gaming.
        print('Okay! . Finally I\'m done!')
    # this doesn't run because we've broken out of the loop.
    print('Can you hear me? ')
    # When you take off R1 an R2, this print above can finally run.
