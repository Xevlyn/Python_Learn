print()

basket = ['a','b','d','c','d','e','f']
## basket.sort()
## print(basket)
print()
# This modifies the list such that the items are placed in the correct order
# Yes. That's how the code is written not like the previous examples

print(sorted(basket))
# This is another method of writing it
# The original basket still remains thesame.
# For this method, it is a completely different basket which is printed out that is sorted
print()
## print(basket)
## print()

basket.copy()
print(basket)
print()

basket.reverse()
print(basket)
print()
# Output ['f', 'e', 'd', 'c', 'd', 'b', 'a']

# In the name it reverses the lists as it is printed
# When you wish to sort and reverse the list. Do the following below
basket.sort()
basket.reverse()
print(basket)

# Output ['f','e','d','d','c','b','a']