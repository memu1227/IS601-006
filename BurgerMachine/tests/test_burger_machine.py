import pytest
# make sure there's an __init__.py in this tests folder and that
# the tests folder is in the same folder as the BurgerMachine stuff
from BurgerMachine import BurgerMachine
from BurgerMachineExceptions import ExceededRemainingChoicesException, InvalidChoiceException, InvalidStageException, OutOfStockException
#this is an example test showing how to cascade fixtures to build up state

@pytest.fixture
def machine():
    bm = BurgerMachine()
    
    return bm

# sample fixture, can delete if not using
'''
@pytest.fixture

def first_order(machine):
    machine.handle_bun("no bun")
    machine.handle_patty("veggie")
    machine.handle_patty("next")
    machine.handle_toppings("done")
    machine.handle_pay(10000,"10000")
    return machine

# sample fixture, can delete if not using
@pytest.fixture
def second_order(first_order):
    first_order.handle_bun("lettuce wrap")
    first_order.handle_patty("turkey")
    first_order.handle_patty("turkey")
    first_order.handle_patty("next")
    first_order.handle_toppings("cheese")
    first_order.handle_toppings("cheese")
    first_order.handle_toppings("done")
    #machine.handle_pay(10000,"10000")
    return first_order

# sample test case, can delete if not using
def test_production_line(second_order):
    for j in second_order.buns:
        print(second_order.inprogress_burger)
        if j.name.lower() == second_order.inprogress_burger[0].name.lower():
            assert True
            return

    assert False
'''

# add required test cases below

#Test 1 - bun must be the first selection (can't add patties/toppings without a bun choice)
def test_bun_first_choice(machine):
    machine.reset()
    #Select a patty without selecting a bun
    with pytest.raises(InvalidStageException):
        machine.handle_patty("veggie")

    # Select a topping without selecting a bun
    with pytest.raises(InvalidStageException):
        machine.handle_toppings("cheese")
    
    #Select a patty and a topping after selecting the bun
    machine.handle_bun("Lettuce Wrap")
    machine.handle_patty("Veggie")
    machine.handle_patty("next")
    machine.handle_toppings("Cheese")

    '''
    UCID: mm2836
    Date Implemented: 3/17/23
    Summary: Tests to see if bun is the first selection
    '''

#Test 2 - can only add patties if they're in stock
def test_patty_stock(machine):
    machine.reset()
    # Set the quantity of the veggie patty to 1
    for patty in machine.patties:
        if patty.name == "Veggie":
            patty.quantity = 1
    machine.handle_bun("Lettuce Wrap")
    machine.handle_patty("veggie")
    with pytest.raises(OutOfStockException):
        machine.handle_patty("veggie")
    machine.handle_toppings("done")

    '''
    UCID: mm2836
    Date Implemented: 3/17/23
    Summary: Checks to see if exception is raised if any patty is out of stock 
    '''

#Test 3 - can only add toppings if they're in stock
def test_toppings_stock(machine):
    machine.reset()
    for patty in machine.patties:
        if patty.name == "Veggie":
            patty.quantity = 10
    for topping in machine.toppings:
        if topping.name == "Cheese":
            topping.quantity = 1
    machine.handle_bun("Lettuce Wrap")
    machine.handle_patty("veggie")
    machine.handle_patty("next")
    machine.handle_toppings("cheese")
    with pytest.raises(OutOfStockException):
        machine.handle_toppings("cheese")
    machine.handle_toppings("done")

    '''
    UCID: mm2836
    Date Implemented: 3/17/23
    Summary: Checks to see if exception is raised if any topping is out of stock 
    '''

#Test 4 - Can add up to 3 patties of any combination
def test_three_patties(machine):
    machine.reset()
    for patty in machine.patties:
        if patty.name == "Veggie":
            patty.quantity = 10
    for topping in machine.toppings:
        if topping.name == "Cheese":
            topping.quantity = 10
    machine.handle_bun("Lettuce Wrap")
    machine.handle_patty("veggie")
    machine.handle_patty("beef")
    machine.handle_patty("turkey")
    with pytest.raises(ExceededRemainingChoicesException):
        machine.handle_patty("turkey")
    machine.handle_toppings("done")

    '''
    UCID: mm2836
    Date Implemented: 3/17/23
    Summary: Ensures that only or atmost 3 patties of any combo can be selected
    '''

#Test 5 - Can add up to 3 toppings of any combination
def test_three_toppings(machine):
    machine.reset()
    for patty in machine.patties:
        if patty.name == "Veggie":
            patty.quantity = 10
    for topping in machine.toppings:
        if topping.name == "Cheese":
            topping.quantity = 10
    machine.handle_bun("Lettuce Wrap")
    machine.handle_patty("veggie")
    machine.handle_patty("next")
    machine.handle_toppings("cheese")
    machine.handle_toppings("tomato")
    machine.handle_toppings("ketchup")
    with pytest.raises(ExceededRemainingChoicesException):
        machine.handle_toppings("bbq")
    machine.handle_toppings("done")
    
    '''
    UCID: mm2836
    Date Implemented: 3/18/23
    Summary: Ensures that only or atmost 3 toppings of any combo can be selected
    '''

#Test 6 - cost must be calculated properly based on the choices (check for currency format as part of this) (test case should have a few permutations of at least 3 valid burgers)
def test_cost(machine):
    for patty in machine.patties:
        if patty.name == "Veggie":
            patty.quantity = 10
    for topping in machine.toppings:
        if topping.name == "Cheese":
            topping.quantity = 10

    #Permutation 1:
    machine.handle_bun("Lettuce Wrap")
    machine.handle_patty("veggie")
    machine.handle_patty("next")
    machine.handle_toppings("cheese")
    machine.handle_toppings("tomato")
    machine.handle_toppings("done")
    cost = machine.calculate_cost()
    assert cost == 3.0

    machine.reset()
    #Permutation 2:
    machine.handle_bun("White Burger Bun")
    machine.handle_patty("turkey")
    machine.handle_patty("next")
    machine.handle_toppings("mayo")
    machine.handle_toppings("tomato")
    machine.handle_toppings("lettuce")
    machine.handle_toppings("done")
    cost = machine.calculate_cost()
    assert cost == 2.75

    machine.reset()
    #Permutation 3:
    machine.handle_bun("Wheat Burger Bun")
    machine.handle_patty("beef")
    machine.handle_patty("next")
    machine.handle_toppings("pickles")
    machine.handle_toppings("ketchup")
    machine.handle_toppings("bbq")
    machine.handle_toppings("done")
    cost = machine.calculate_cost()
    assert cost == 3.0

    '''
    UCID: mm2836
    Date Implemented: 3/18/23
    Summary: 
    '''

#Test 7 - Total Sales (sum of costs) must be calculated properly (test case should have a few permutations of at least 3 valid burgers)
def test_total_sales(machine):
    for patty in machine.patties:
        if patty.name == "Veggie":
            patty.quantity = 10
    for topping in machine.toppings:
        if topping.name == "Cheese":
            topping.quantity = 10

    #Permutation 1:
    machine.handle_bun("Lettuce Wrap")
    machine.handle_patty("veggie")
    machine.handle_patty("next")
    machine.handle_toppings("cheese")
    machine.handle_toppings("tomato")
    machine.handle_toppings("done")
    machine.handle_pay(3.0,"3.0")

    #Permutation 2:
    machine.handle_bun("White Burger Bun")
    machine.handle_patty("turkey")
    machine.handle_patty("next")
    machine.handle_toppings("mayo")
    machine.handle_toppings("tomato")
    machine.handle_toppings("lettuce")
    machine.handle_toppings("done")
    machine.handle_pay(2.75,"2.75")
    
    #Permutation 3:
    machine.handle_bun("Wheat Burger Bun")
    machine.handle_patty("beef")
    machine.handle_patty("next")
    machine.handle_toppings("pickles")
    machine.handle_toppings("ketchup")
    machine.handle_toppings("bbq")
    machine.handle_toppings("done")
    machine.handle_pay(3.0,"3.0")

    assert machine.total_sales == 8.75

    '''
    UCID: mm2836
    Date Implemented: 3/18/23
    Summary: Checks to see if the total cost of all burger orders is accurate
    '''

#Test 8 - Total burgers should properly increment for each purchase
def test_total_burgers(machine):
    #initialize burger count to initially be zero
    machine.total_burgers = 0
    for patty in machine.patties:
        if patty.name == "Veggie":
            patty.quantity = 10
    for topping in machine.toppings:
        if topping.name == "Cheese":
            topping.quantity = 10

    #Permutation 1:
    machine.handle_bun("Lettuce Wrap")
    machine.handle_patty("veggie")
    machine.handle_patty("next")
    machine.handle_toppings("cheese")
    machine.handle_toppings("tomato")
    machine.handle_toppings("done")
    machine.handle_pay(3.0,"3.0")
    assert machine.total_burgers == 1

    #Permutation 2:
    machine.handle_bun("White Burger Bun")
    machine.handle_patty("turkey")
    machine.handle_patty("next")
    machine.handle_toppings("mayo")
    machine.handle_toppings("tomato")
    machine.handle_toppings("lettuce")
    machine.handle_toppings("done")
    machine.handle_pay(2.75,"2.75") 
    assert machine.total_burgers == 2

    #Permutation 3:
    machine.handle_bun("Wheat Burger Bun")
    machine.handle_patty("beef")
    machine.handle_patty("next")
    machine.handle_toppings("pickles")
    machine.handle_toppings("ketchup")
    machine.handle_toppings("bbq")
    machine.handle_toppings("done")
    machine.handle_pay(3.0,"3.0")
    assert machine.total_burgers == 3

    '''
    UCID: mm2836
    Date Implemented: 3/18/23
    Summary: Checks to make sure the total burger count is incremented after each order
    '''
