"""Testing Subtraction"""
from calc.calculations.division import Division

def test_calculation_division():
    """testing that our calculator has a static method for addition"""
    #Arrange
    mynumbers = (1.0, 2.0)
    division = Division(mynumbers)
    #Act
    #Assert
    assert division.get_result() == 0.5

    mynumbers = (4.0, 2.0)
    division = Division(mynumbers)
    assert division.get_result() == 2.0

    mynumbers = (100.0, 2.0)
    division = Division(mynumbers)
    assert division.get_result() == 50.0
