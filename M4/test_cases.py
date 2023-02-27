#import pytest 
import pytest
from MyCalc import MyCalc

#Test Cases
#test addition
def test_add():
    calc = MyCalc()
    #test all the pos and neg value combos
    assert calc.addition(4,3) == 7
    assert calc.addition(-4, 3) == -1
    assert calc.addition(4, -3) == 1
    assert calc.addition(-4, -3) == -7
    '''
    UCID: mm2836
    Date Implemented: 02/26/23
    Summary: Trying diff number sign combos for test cases for addition
    '''

#test the add ans
def test_add_ans():
    calc = MyCalc()
    calc.addition(-4,-3)
    assert calc.addition('ans',7) == 0
    calc.addition(-7,7)
    assert calc.addition(7,'ans') == 7
    '''
    UCID: mm2836
    Date Implemented: 02/26/23
    Summary: Trying diff number sign combos for test cases ans for addition
    '''

#test subtraction
def test_sub():
    calc = MyCalc()
    #test all the pos and neg value combos
    assert calc.subtraction(4,3) == 1
    assert calc.subtraction(-4, 3) == -7
    assert calc.subtraction(4, -3) == 7
    assert calc.subtraction(-4, -3) == -1
    '''
    UCID: mm2836
    Date Implemented: 02/26/23
    Summary: Trying diff number sign combos for test cases for subtraction
    '''

#test the ans
def test_sub_ans():
    calc = MyCalc()
    calc.subtraction(-4,-3)
    assert calc.subtraction('ans',7) == -8 
    calc.subtraction(-4,4)
    assert calc.subtraction(7,'ans') == 15
    '''
    UCID: mm2836
    Date Implemented: 02/26/23
    Summary: Trying diff number sign combos for test cases ans for subtraction
    '''

#test multiplication
def test_mult():
    calc = MyCalc()
    #test all the pos and neg value combos
    assert calc.multiplication(4,3) == 12
    assert calc.multiplication(-4, 3) == -12
    assert calc.multiplication(4, -3) == -12
    assert calc.multiplication(-4, -3) == 12
    '''
    UCID: mm2836
    Date Implemented: 02/26/23
    Summary: Trying diff number sign combos for test cases for multiplication
    '''

#test the ans
def test_mult_ans():
    calc = MyCalc()
    calc.multiplication(4,3)
    assert calc.multiplication('ans',7) == 84 
    calc.multiplication(12,7)
    assert calc.multiplication(7,'ans') == 588
    '''
    UCID: mm2836
    Date Implemented: 02/26/23
    Summary: Trying diff number sign combos for test cases ans for multiplication
    '''

#test division
def test_div():
    calc = MyCalc()
    #test all pos and neg value combos
    assert calc.division(8,2) == 4
    assert calc.division(-8, 2) == -4
    assert calc.division(8, -2) == -4
    assert calc.division(-8, -2) == 4
    #test zero values
    with pytest.raises(ZeroDivisionError):
        calc.division(8, 0)
    '''
    UCID: mm2836
    Date Implemented: 02/26/23
    Summary: Trying diff number sign combos for test cases for division
    '''

#test the ans
def test_div_ans():
    calc = MyCalc()
    calc.division(8,2)
    assert calc.division('ans',2) == 2
    calc.division(4,2)
    assert calc.division(2,'ans') == 1
    #test zero as ans
    calc.addition(4,-4)
    with pytest.raises(ZeroDivisionError):
        calc.division(4,'ans')
    '''
    UCID: mm2836
    Date Implemented: 02/26/23
    Summary: Trying diff number sign combos for test cases ans for division
    '''


