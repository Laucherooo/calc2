"""Testing the Calculator"""
from calculator.main import Calculator

def test_calculator_result():
    """testing calculator result is 0"""
    calc = Calculator()
    assert calc.result == 0

def test_calculator_add():
    """Testing the Add function of the calculator"""
    #Arrange by instantiating the calc class
    calc = Calculator()
    #Act by calling the method to be tested
    calc.add_number(4)
    #Assert that the results are correct
    assert calc.result == 4

def test_calculator_get_result():
    """Testing the Get result method of the calculator"""
    calc = Calculator()
    calc.add_number(1)
    assert calc.get_result() == 1

def test_calculator_subtract():
    """Testing the subtract method of the calculator"""
    calc = Calculator()
    calc.subtract_number(1)
    assert calc.get_result() == -1

def test_calculator_multiply():
    """ testing multiplication"""
    calc = Calculator()
    result = calc.multiply_numbers(1,2)
    assert calc.get_result() == 2

def test_add_subtract_multiple_divide():
    """ testing add, subtract, multiple and divide"""
    calc = Calculator()
    result = calc.add_number(5)
    assert calc.get_result() == 5

    calc = Calculator()
    result = calc.subtract_number(5)
    assert calc.get_result() == -5

    calc = Calculator()
    result = calc.multiply_numbers(5, 5)
    assert calc.get_result() == 25

    calc = Calculator()
    result = calc.divide_number(0, 5)
    assert calc.get_result() == 0