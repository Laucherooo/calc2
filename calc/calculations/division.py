"""Addition Class"""
from calc.calculations.calculation import Calculation

class Division(Calculation):
    """ calculation addition class"""
    def get_result(self):
        """get the division results"""
        D_values = 0.0
        for value in self.values:
            if(D_values == 0.0):
                D_values = value
                continue
            D_values = D_values / value
        return D_values
