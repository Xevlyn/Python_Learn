def highest_even(li):
    #separate the even from the odd
    even = []
    # Select the even numbers by looping through the list parameter
    for item in li:
        if item % 2 == 0:
            even.append(item) # add to the even list
        return max(even) #Sort the highest even number in the even list created


print(highest_even([10,2,3,4,6,8,11]))
