# A dictionary key has to be immutable and must be descriptive
# A key has to be unique and can only exist once else the other will be overide

dictionary = {
    123: [1, 2, 3],
    True: 'Hello',
    'is_magic': True

}

print(dictionary[True])
print()
print(dictionary['is_magic'])
