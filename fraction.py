from fractions import Fraction

# Creating fractions
frac1 = Fraction(3, 4)  # 3/4
frac2 = Fraction(1.5)   # Converts float to 3/2
frac3 = Fraction("7/8") # From string

# Arithmetic operations
result = frac1 + frac2  # Adds fractions
print(result)           # Output: 9/4

# Accessing numerator and denominator
print(result.numerator)   # 9
print(result.denominator) # 4

frac4 = Fraction(4, 1)
print(frac4)

frac5 = Fraction(10, 4)
print(frac5)