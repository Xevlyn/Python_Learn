# Look up the documentation for this on the python website
print(len('Diego Maradona'))
# index count begins from 1 and not 0 in this case
# Built-in functions have the syntax of the word and () to perform an action on a datatype where as methods are similar but they are owned by something
print()
quote = 'to be or not to be'
print(quote.upper())  # Turns the entire word into uppercases
print(quote.capitalize())  # Capitalizes the first letter of the first word
print(quote.lower())  # Lower cases every word
print(quote.find('be'))  # locates the first occurrence of the desired word

# Replaces all the occurrences of the previous word

print(quote.replace('be', 'me'))

print(quote)
# The original quote still doesn't change bcs it is immutable but it has been modified but assigned to different values hence making them separate from the first one
