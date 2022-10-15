import random
land = [1, 2, 3, 4, 5]

print(random.random())  # Gives a random number btwn 0 and 1
print(random.randint(0, 9))  # Gives a random number
print(random.choice([1, 2, 3]))
random.shuffle(land)
print(land)

# help(random) gives you more information on the function

# random has randomly a random method

# Best practice is to be explicit with the file you're coding and the built in function you choose.
