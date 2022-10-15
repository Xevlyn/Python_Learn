# While condition do action
i = 0
while i < 50:
    #i += 1 putting this here prints with 50 inclusive
    # This is because when placed here the initial value is no longer 0 bu 1 adn the increment count will begin from one.n
    print(i)
    #infinite loop
    # while i < 50:
    # print(i)

    # This can crash a system 
    i += 1
    # i is incremented by 1 until condition is met
    # if there was a break above here
    # the code would have stopped running hence the else won't execute,
else:
    print('Done with all the work')
    # this is executed when all the increments are completed above
print()