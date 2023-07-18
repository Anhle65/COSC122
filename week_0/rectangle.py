
class Fraction():
    '''Defines a Fraction type that has an integer numerator and a non-zero integer denominator'''

    def __init__(self, num=0, denom=1):
        ''' Creates a new Fraction with numerator num and denominator denom'''
        self.numerator = num
        if denom != 0:
            self.denominator = denom
        else:
            raise ZeroDivisionError
            
    def __str__(self):
        """represent the Fraction"""
        return f"{self.numerator}/{self.denominator}"
    
    def __repr__(self):
        return f"Fraction({self.numerator}, {self.denominator})"
    def __add__(self, other):
        '''Return a new unreduced fraction obtained by adding other to self'''
        # Only submit your __add__ method here!
        denominator =  self.denominator * other.denominator
        numerator = (self.numerator * other.denominator ) + (other.numerator * self.denominator)
        return Fraction(numerator, denominator)
    
    def __mul__(self, other):
        '''Implement the multiply operator'''
        numerator = self.numerator * other.numerator
        denominator = self.denominator * other.denominator
        return Fraction(numerator,denominator)

    def __eq__(self, other):
        """Implement the '==' operator on Fractions"""
        if self.denominator * other.numerator == other.denominator * self.numerator:
            return True
        else:
            return False

def find_gcd(num1, num2):
    """ 
    Returns the Greatest Common Divisor (GCD) of num1 and num2. 
    Assumes num1 and num2 are positive integers. 
    """
    smaller = min(num1, num2)
    for i in range(smaller, 1, -1):
        if num1 % i == 0 and num2 % i == 0:
            return i
    return 1
    
    
class ReducedFraction(Fraction):
    '''A version of Fraction that always keeps itself in maximally reduced form'''
    
    def __init__(self, numerator=0, denominator=1):
        """ Initialiser, given both numerator and denominator """

        # Look out for student section comments
        # You should fill in these sections with appropriate code, that is,
        # The pass should be replaced with one or more lines of code...
        # ---start student section---
        super().__init__(numerator, denominator)
        self.__reduce__()
        # ===end student section===

    def __reduce__(self):
        """simplified fraction"""
        # You will need to add a docstring
        # then replace the below pass with your code
        # which will be more than one line...
        # ---start student section---
        common = find_gcd(self.numerator, self.denominator)
        self.numerator = int(self.numerator // common)
        # print(new_nu)
        self.denominator = int(self.denominator // common)
        return Fraction(self.numerator, self.denominator)
        # ===end student section===

    def __repr__(self):
        # You will need to add a docstring
        # then replace the below pass with your code
        # which will be more than one line...
        # ---start student section---
        """represent the Fraction"""
        return f"ReducedFraction({self.numerator}, {self.denominator})"
        # ===end student section===

    def __add__(self, other):
        # You know the deal
        # ---start student section---
        '''Return a new unreduced fraction obtained by adding other to self'''
        # Only submit your __add__ method here!
        denominator =  self.denominator * other.denominator
        numerator = (self.numerator * other.denominator ) + (other.numerator * self.denominator)
        return ReducedFraction(numerator, denominator)
        # ===end student section===

    def __mul__(self, other):
        '''Implement the multiply operator'''
        numerator = self.numerator * other.numerator
        denominator = self.denominator * other.denominator
        return ReducedFraction(numerator,denominator)
class MixedNumber():
    def __init__(self, number, fraction):
        """a mixed number"""
        self.number = number
        residual = fraction.numerator // fraction.denominator
        if  residual != 0:
            fraction.numerator -= residual * fraction.denominator
            self.number += residual
        self.fraction = ReducedFraction(fraction.numerator, fraction.denominator)
        # self.fraction = fraction

    def __str__(self):
        """return string stating the whole part"""
        return f"{self.number} and {self.fraction}"
    def __repr__(self):
        """represent a mixed number"""
        return (f'MixedNumber({self.number}, '
                f'ReducedFraction{self.fraction.numerator, self.fraction.denominator})')

    def __add__(self, other):
        number = self.number + other.number
        fraction = self.fraction + other.fraction
        return MixedNumber(number, fraction)

x = MixedNumber(3, Fraction(1, 3))
y = MixedNumber(-1, Fraction(2, 5))
z = x + y
print(z)
print(repr(z))