#Script does basic mathematic operations (add/subtract/multiply/division) and test cases
#These functions should update an internal variable as a running total/value called ans
#All functions must properly handle the math given standard math scenarios (i.e., show proper messages when trying to divide by zero for example)

#create a class that essentially does the basic mathematical operations
class MyCalc:
    #initialize answer
    ans = 0
    #check data type of input
    #check for float
    def check_float(self, val):
        try:
            val = float(val)
            return True
        except:
            return False

    #check for integer
    def check_int(self, val):
        try:
            val = int(val)
            return True
        except:
            return False

    #check for number
    def check_num(self, val):
        if self.check_int(val):
            return int(val)
        elif self.check_float(val):
            return float(val)
        else:
            raise Exception("Not a number")
    '''
    UCID: mm2836
    Date Implemented: 02/25/23
    Summary: *Code adapted from Professor's class example from his Github* - Checks the data type of the values 
    '''
    def __init__(self):
        self.ans == 0

    #addition
    def addition(self,x,y):
        #check to see if one of the values is the previous answer
        if x == "ans":
            return self.addition(self.ans,y)
        elif y == "ans":
            return self.addition(x,self.ans)
        else:
            x = self.check_num(x)
            y = self.check_num(y)
            self.ans = x + y
        return self.ans
    '''
    UCID: mm2836
    Date Implemented: 02/25/23
    Summary: Checks if either value is equal to answer and then adds the numbers together 
    '''
    #subtraction
    def subtraction(self,x,y):
        #check to see if one of the values is the previous answer
        if x == "ans":
            return self.subtraction(self.ans,y)
        elif y == "ans":
            return self.subtraction(x,self.ans)
        else:
            x = self.check_num(x)
            y = self.check_num(y)
            self.ans = x - y
        return self.ans
    '''
    UCID: mm2836
    Date Implemented: 02/25/23
    Summary: Checks if either value is equal to answer and then subtracts the numbers 
    '''

    #multipllication
    def multiplication(self,x,y):
        #check to see if one of the values is the previous answer
        if x == "ans":
            return self.multiplication(self.ans,y)
        elif y == "ans":
            return self.multiplication(x,self.ans)
        else:
            x = self.check_num(x)
            y = self.check_num(y)
            self.ans = x * y
        return self.ans
    '''
    UCID: mm2836
    Date Implemented: 02/25/23
    Summary: Checks if either value is equal to answer and then multiplies the numbers together 
    '''

    #division
    def division(self,x,y):
        #check to see second number isnt zero 
        if y == 0:
            raise ZeroDivisionError("Cannot divide by zero")
        #check to see if one of the values is the previous answer
        if x == "ans":
            return self.division(self.ans,y)
        elif y == "ans":
            if "ans" == 0:
                raise ZeroDivisionError("Cannot divide by zero")
            return self.division(x,self.ans)
        else:
            x = self.check_num(x)
            y = self.check_num(y)
            self.ans = x / y 
        return self.ans 
    '''
    UCID: mm2836
    Date implemented: 02/25/23
    Summary: Checks to see if the second value entered is zero or if either of the values is equal to the previous answer and then divides the numbers
    '''

#main 
def main():
    calc = MyCalc()
    while True:
        #user input
        eq = input("Enter equation: ").strip()
        if eq == "q" or "quit":
            break

        #addition
        if "+" in eq:
            #split based on operator
            sep = eq.split("+")
            #set num 1 and num2 equal to individual numbers
            num1 = sep[0].strip()
            #print(num1)
            num2 = sep[1].strip()
            #print(num2)
            #do the calculation
            MyCalc.addition(num1,num2)
            '''
            UCID: mm2836
            Date Implemented: 02/25/23
            Summary: looks for the addition operator and then separates out the individual values before calling the function to add the numbers
            '''

        #multiplication
        elif ("*" in eq) or ("x" in eq):
            if "*" in eq:
                #split on operator
                sep = eq.split("*")
            elif "x" in eq:
                #split on operator
                sep = eq.split("x")
            #set num 1 and num2 equal to individual numbers
            num1 = sep[0].strip()
            num2 = sep[1].strip()
            #do the calculation
            MyCalc.multiplication(num1,num2)
            '''
            UCID: mm2836
            Date Implemented: 02/25/23
            Summary: looks for the multiplication operators and then separates out the individual values before calling the function to multiply the numbers
            '''

        #division
        elif "/" in eq:
            #split on operator
            sep = eq.split("/")
            #set num1 and num2 equal to individual numbers
            num1 = sep[0].strip()
            num2 = sep[1].strip()
            #do the calculation
            MyCalc.division(num1,num2)
            '''
            UCID: mm2836
            Date Implemented: 02/25/23
            Summary: looks for the division operator and then separates out the individual values before calling the function to multiply the numbers
            '''

        #subtraction (done last to handle negative values)
        elif "-" in eq:
            #split on operator
            sep = eq.split("-")
            #set num 1 and num2 equal to individual numbers
            num1 = sep[0].strip()
            num2 = sep[1].strip()
            #do the calculation
            MyCalc.subtraction(num1,num2)
            '''
            UCID: mm2836
            Date Implemented: 02/25/23
            Summary: looks for the subtraction operator and then separates out the individual values before calling the function to multiply the numbers
            '''

        #for invalid operator    
        else:
            print("Invalid Operator")
    

if __name__ == "__main__":
    main()   

'''
UCID: mm2836
Date Implemented: 02/26/23
Summary: runs the main function 
'''
    
    
    