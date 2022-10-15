# Set comprehensions are similar to the comprehensions with lists
# Sets only allow unique values and not duplicates

my_list1 = {char for char in 'Hello'}
my_list2 = {num for num in range(0, 100)}

my_list3 = {num**2 for num in range(0, 100)}

print(my_list1)
print()


# Dictionary comprehensions
simple_dict = {
    'a': 1,
    'b': 2

}
my_dict = {key: value**2 for key, value in simple_dict.items() if value %
           2 == 0}

# key value per where the item is the key and the item multiplied by 2 is the value
my_dict2 = {num: num*2 for num in [1, 2, 3]}

print()
print(my_dict2)
