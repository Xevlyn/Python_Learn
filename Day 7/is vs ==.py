print()
print(True == 1)
print()
print('1' == 1)
print()
print([] == 1)
print()
print(10 == 10.0)
print()
print([] == [])
print()

# The == checks for equality of value  and knowing that the truthy for 1 is true and that for 0 is falsey hence false
# The boolean type  is converted for the strings on the right hand side of the equation for the boolean type conditions

print()
print(True is True)
print()
print('1' is '1')
print()
print([]  is []) #This is false because these [] are 2 completely diffrent ones since they are in diffrent locations
# Same applies to dictionaries and tuples ie they're saved in diffrent locations
print()
print(10 is 10.0)
print()
print([1,2,3] is  [1,2,3]) #This is false because these [] are 2 completely diffrent ones since they are in diffrent locations
print()

# The output here is all FALSE because it checks if the location and memory where the value is stored is thesame. except the first 2