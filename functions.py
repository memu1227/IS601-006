def myFunc():
    print("This is my awesome function")

#myFunc()

#tuples: immutable items - cant change a tuple, works the same way as a list

def myTfunc(*args):
    print(f"{args}")

#myTfunc("hi", "bye", "hello")

def myKFunc(**args):
    print(f"{args}")

#myKFunc(name = "Bob", age = 50, job = "Painter")

def myDFunc(val, name = "World"):
    print(f"Hello, {name} val : {val}")
    #put required values first so if only one arguemnt is given, itll assign that value to required value

#myDFunc()
#myDFunc("Megha")

#pass: keyword to avoid error
def add(a,b):
    pass

