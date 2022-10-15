def outer():
    x = "Local"
    def inner():
        nonlocal x
        x = "nonlocal" 
        # new string is assigned to x replacing the old string called local
        print("inner:", x)

    inner()
    print("outer:", x)

outer()

# The nonlocal keyword is used to refer to the parent local ie a way to say you want to use a variable out of the scope function which isn't a global variable.