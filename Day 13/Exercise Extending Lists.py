class SuperList(list):
    def __len__(self):
        return 1000


super_list1 = SuperList()

print(len(super_list1))
super_list1.append(5)
print(super_list1[0])
print()
# The functionality of list is extended.
# To verify do th following

print(issubclass(list, object))
