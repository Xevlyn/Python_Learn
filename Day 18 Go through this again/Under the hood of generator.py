# def special_for(iterable):
#    iterator = iter(iterable)
#    while True:
#       try:
#            print(iterator)
#            next(iterator)  # Looped through some iterable objects using next()
#        except StopIteration:
#            break


# special_for([1, 2, 3])  # These objects exist in thesame memory space
# The about above code loops through thesame memory space.

# Applying it to range()

# The code below isn't running. Said the problem is at line 36 which I still haven't recognized is there.

class MyGen():
    current = 0

    def __init__(self, first, last):
        self.first = first
        self.last = last


def __iter__(self):
    return self


def __next__(self):
    # How we want next to work  and state or data to keep track.
    if MyGen.current < self.last:
        num = MyGen.current
        MyGen.current += 1
        return num
    raise StopIteration


gen = MyGen(0, 100)  # Works using the dunder methods
for i in gen:
    print(i)


# You don't need to know this.
