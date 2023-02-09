#PYTHON IS A LOOSELY TYPED LANGUAGE

class Person:
    name = "bob"
    age = 50
    job = "Painter"
    def __init__(self) -> None:
        self.name = "Megha"
        self.age = 25
        self.job = "Student"
    def __repr__(self) -> str:
        return(f"{self.name}, {self.age}, {self.job}")

person = Person()

#dictionary
print(f"{person.__dict__}")

#classs level data
print(f"{Person.__dict__}")
#Constructor: runs when a class is exteniated (init is constructor)

#parameters are used during function definitions 
#arguments are used when functions are called

#function: dont belong anywhere, stand alone
#method: functions that belong to a class

#instance method:method that runs per object, related to the object, have self parameter, belongs to instance of a class
    #belongs to object
#class method: same method across all objects, will typically give same answer
    #belongs to class

#property: in a class
#variable: things designed whereever

#2 underscores: private (harder to access)

#inheritance: think ab common denominator