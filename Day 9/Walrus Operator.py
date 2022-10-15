# :=  Walrus operator / Assignment expression
# This operator is used to assign values to variables as part of a larger expression.

a = "Hellooooooooooo"
if ((f := len(a)) > 10): 
    # the length of the variable a is now assigned to n using the walrus operator and n can now be used to return the length of the variables present
    print(f"too long {f} elements")
while ((n := len(a)) > 1):
    print(n)
    a = a[:-1]
print()
print(a)
print()