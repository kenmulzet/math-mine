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
    
    def get_num_terms(self):
        terms = 0
        for i in range(len(self.coefficients)):
            if self.coefficients[i] != 0:
                terms += 1

        return terms
        
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
        for i in range(self._degree + 1):
            num = self.coefficients[i]
            new_coefficients.append(Fraction(num, i + 1))

        return Polynomial(new_coefficients)

class Exponential:
    def __init__(self, coeff_fn, exponential_fn):
        if not (isinstance(coeff_fn, Polynomial) and isinstance(exponential_fn, Polynomial)):
            raise TypeError("Both functions must be of type Polynomial.")

        self._coeff = coeff_fn
        self._exponent = exponential_fn

    def __str__(self):
        coeff = str(self._coeff)
        exp = str(self._exponent)
        if self._coeff.get_degree() == 0:
            return f" {coeff} e^{{{exp}}}"
        else:
            return f"( {coeff} ) e^{{{exp}}}"

    def derivative(self):
        new_coeff = self._coeff.derivative() + self._coeff * self._exponent.derivative()
        new_function = Exponential(new_coeff, self._exponent)
        return new_function
    
class Trig:
    def __init__(self, function, coefficient, argument):
        if function not in (r"\sin", r"\cos", r"\tan", r"\cot", r"\sec", r"\csc"):
            raise TypeError("Invalid choice of function.")
        if not isinstance(coefficient, Polynomial):
            raise TypeError("Coefficient function must be of type Polynomial.")
        if not isinstance(argument, Polynomial):
            raise TypeError("Argument function must be of type Polynomial.")
        
        self._function = function
        self._coefficient = coefficient
        self._argument = argument

    def derivative(self):

        answer = ""
        if self._coefficient.get_degree() > 0:
            answer = "(" + str(self._coefficient.derivative()) + ") " + self._function + "(" + str(self._argument) + ")"
            str(self._coefficient.derivative()) + self._function + "(" + str(self._argument) + ")"

        if self._function == r"\sin":
            answer += "+ (" + str(self._coefficient * self._argument.derivative()) + r") \cos (" + str(self._argument) + ")"
        elif self._function == r"\cos":
            answer += "- (" + str(self._coefficient * self._argument.derivative()) + r") \sin (" + str(self._argument) + ")"
        elif self._function == r"\tan":
            answer += "+ (" + str(self._coefficient * self._argument.derivative()) + r") \sec^2 (" + str(self._argument) + ")"
        elif self._function == r"\cot":
            answer += "- (" + str(self._coefficient * self._argument.derivative()) + r") \sec^2 (" + str(self._argument) + ")"
        elif self._function == r"\sec":
            answer += "+ (" + str(self._coefficient * self._argument.derivative()) + r") \sec (" + str(self._argument) + r") \tan (" + str(self._argument) + ")"
        elif self._function == r"\csc":
            answer += "- (" + str(self._coefficient * self._argument.derivative()) + r") \csc (" + str(self._argument) + r") \cot (" + str(self._argument) + ")"

        return f"{answer}"