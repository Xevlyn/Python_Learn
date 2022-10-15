print()
my_tuple = (1,2,3,4,5)
print(my_tuple)
print()

new_tuple = my_tuple[1:4]
new_tuple2 = my_tuple[1:2]
print(new_tuple)
print()
print(new_tuple2) #Though it contains a comma it's still a tuple.
print()

x,y,z, *other = (1,2,3,4,5)
print(x)
print(y)
print(z)
print(other)
print()


# Tuple Method: Count#
print(my_tuple.count(5))
print() 
# Tuple Method: Index#
print(my_tuple.index(5)) 