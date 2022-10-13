selfish = '12345678'
# 01234567 These are the indexes of the above

print(selfish[0:4])

print()

# When we use the [] in python, the first item has the index 0 and its called the start and stop has the index 7
# Using the example above there are 8 indexes starting from 0 and ending at 7

# Stepovers
# When the string is written as [0:5:2] it will print the indexes from 0 to 5 stepping over indexes by 2
print(selfish[0:8:2])
print()
print(selfish[1:])  # Starts from index 1 and ends at the last index
print()
print(selfish[:5])  # Start from the 0 index and stop at the index 5
print()
print(selfish[::2])  # Start from the first and end at the last skipping by 2
print()
# Negative indexes which means start from the end of the string since its counting backwards
print(selfish[-1])
print()
print(selfish[::-2])  # Indexes  in reverse and steped over  by 2
print()
print(selfish[::-1])  # Indexes in reverse and steped over by 1
# [Start:Stop:Stepover]
