def do_twice(func):
    def wrapper__do_twice(*args,**kwargs):
        func(*args,**kwargs)
        func(*args,**kwargs)
        func(*args,**kwargs)
        #one asterix: tuple
        #two asterix: dictionary
    return wrapper__do_twice

@do_twice
def say_hello(name):
    print(f"Hello {name}")

@do_twice
def say_bye():
    print("bye")

@do_twice
def add(a,b):
    print(a+b)

say_hello("Megha")
say_bye()
add(5,2)

#decorators can apply to any function which is why decorator 
#should be able to work with any arguments

#assert checks to see if its true or false