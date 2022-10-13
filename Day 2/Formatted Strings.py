name = 'John'
age = 24
print('hi '+ name +'. You are ' + str(age) + ' years old')
#Main way in python2
print( )

print(f'Hello {name}. You are {age} years old')
print()
#f indicates that the program will be a formatted string and this makes it able to provide the variables which have been called in the {}
#Main way in python3

print('Hey {}. You are {} years old'.format(name, age))
#Dynamic code and advisable to be used in every situation
print()
print('Heya {}. You are {} years old'.format('John','24'))
#Another way of writing the formatted string
#But this is fixed and can't be changed so won't be goof to use most of the time.

#Also when deciding the input completely new variables using this method, make sure to write the values in the {} of the string.
print()
print('Aloha {new_name}. Today you turn {new_age}. Unbelievable!'.format(new_name='Micheal', new_age = 28))