print()

username = '12345'
password = 'kanada'


# When the values used in the conditional statements are of diffrent datatype besides boolean, 
# at the point of the if statement below, when the values are recalled, they are automatically converted to boolean type
# Meaning when the 'Gunners' is called this is what actually happens bool('Gunner')
# The conditional statements don't care about the present datatype the value occupy because they're eventually changed.

## print(bool('Gunners')) ##
## print() ##
## print(bool(5)) ##
## print() ##
## it is a Truthy value reason being that when the boolean type conversion is runned on the value it returns True as the  output  ##

## print(bool('')) ##
## print() ##
## print(bool(0)) ##
## print() ##

# Falsey values on the other hand are values which when the boolean type conversion is runned on the value it returns False as the output
# All values but these are considered to be Falsey values
#
# None, False, 0, 0.0, 0j, Decimal(0), Fraction(0,1),[],{},(),'',b'',set()


if username and password:
    print('You\'re old enough to drive')
    print()
else:
    print()
    print('You are not of age!')

print()
print('Okokok')
print() 