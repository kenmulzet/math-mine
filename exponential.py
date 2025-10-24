from fractions import Fraction

class Polynomial:
    """
    Represents a polynomial with coefficients of type Fraction.
    Coefficients are stored in a list, where the index corresponds to the exponent.
    e.g., [Fraction(1, 2), Fraction(0), Fraction(3, 1)] represents 0.5 + 3x^2
    """
    def __init__(self, coefficients):
        if not all(isinstance(c, Fraction) for c in coefficients):
            raise TypeError("All coefficients must be of type Fraction.")
        
        # Remove trailing zero coefficients to maintain a canonical representation
        while coefficients and coefficients[-1] == Fraction(0):
            coefficients.pop()
        
        self.coefficients = coefficients if coefficients else [Fraction(0)]
        if len(coefficients) == 0:
            self._degree = 0
        else:
            self._degree = len(coefficients) - 1

    def __repr__(self):
        return f"Polynomial({self.coefficients})"
    
    def __str__(self):
        terms = []
        for i, coeff in enumerate(self.coefficients):
#            j = self._degree - i

            if coeff == Fraction(0):
                continue
            
            coeff_str = str(coeff)
            if coeff == Fraction(1) and i > 0:
                coeff_str = ""
            elif coeff == Fraction(-1) and i > 0:
                coeff_str = "-"

            if i == 0:
                terms.append(coeff_str)
            elif i == 1:
                terms.append(f"{coeff_str}x")
            else:
                terms.append(f"{coeff_str}x^{i}")
        
        if not terms:
            return "0"
        
        return " + ".join(terms).replace("+ -", "- ")

    def __add__(self, other):
        if not isinstance(other, Polynomial):
            raise TypeError("Can only add Polynomial objects.")
        
        max_len = max(len(self.coefficients), len(other.coefficients))
        new_coefficients = [Fraction(0)] * max_len
        
        for i in range(len(self.coefficients)):
            new_coefficients[i] += self.coefficients[i]
        for i in range(len(other.coefficients)):
            new_coefficients[i] += other.coefficients[i]
            
        return Polynomial(new_coefficients)

    def __mul__(self, other):
        if not isinstance(other, Polynomial):
            raise TypeError("Can only multiply Polynomial objects.")
        
        len_self = len(self.coefficients)
        len_other = len(other.coefficients)
        new_coefficients = [Fraction(0)] * (len_self + len_other - 1)
        
        for i in range(len_self):
            for j in range(len_other):
                new_coefficients[i + j] += self.coefficients[i] * other.coefficients[j]
                
        return Polynomial(new_coefficients)

    def get_degree(self):
        return self._degree
        
    def get_str(self):
        return self.__str__
    
    def evaluate(self, x):
        """Evaluates the polynomial at a given value x."""
        result = Fraction(0)
        for i, coeff in enumerate(self.coefficients):
            result += coeff * (Fraction(x) ** i)
        return result

    def derivative(self):
        """Returns a new Polynomial representing the derivative."""
        if len(self.coefficients) <= 1:
            return Polynomial([Fraction(0)])
        
        new_coefficients = []
        for i in range(1, len(self.coefficients)):
            new_coefficients.append(self.coefficients[i] * Fraction(i))
            
        return Polynomial(new_coefficients)
    
    def antiderivative(self):
        """Return a new Polynomial representing the antiderivative."""
        new_coefficients = [Fraction(0)]
        print(self.coefficients)
        for i in range(self._degree + 1):
            num = self.coefficients[i]
            print(num)
            new_coefficients.append(Fraction(num, i + 1))
            print(new_coefficients)

        return Polynomial(new_coefficients)
