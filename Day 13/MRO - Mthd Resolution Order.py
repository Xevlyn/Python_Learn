# What is MRO
# D has multiple inheritance from B and C
# while B and C have inheritance from A.
# Method Resolution Order is a rule that python follows to determine when you run a method which one to run.


class A:
    num = 10


class B(A):
    pass


class C(A):
    num = 1


class D(B, C):
    pass


print(D.num)
print()
# This shows the order by which the compiler checks the objects.
print(D.mro())

# 1 is printed at the output
# This is because the MRO goes D B C A. It's important to note that this follows what goes first inline.
print()


class X:
    pass


class Y:
    pass


class Z:
    pass


class A(X, Y):
    pass


class B(Y, Z):
    pass


class M(B, A, Z):
    pass


print(M.mro())
# Order M B A X Y Z object
# It doesn't go to Z regardless of it being connected to it due to the algorithm used to make MRO which is depth for search.
# Not you will never get tested on this.
# This is overly complicated
