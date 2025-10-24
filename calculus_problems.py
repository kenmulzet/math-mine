import random
import functions as fn
from fractions import Fraction

def generate_polynomial(max_degree = 6):
    a = random.randint(1, max_degree)
    coefficients = []
    for i in range(a):
        next_coeff = random.randint(-10, 10)
        coefficients.append(Fraction(next_coeff))
    leading_coeff = random.randint(1, 10)
    coefficients.append(Fraction(leading_coeff))

    polynomial = fn.Polynomial(coefficients)
    return polynomial

def generate_indefinite_integral():

    # Build polynomial
    polynomial = generate_polynomial()

#   Build question and answer strings
    question = f"Calculate the following antiderivative: $$\\int ({polynomial})\\,dx$$"
    answer = f"${polynomial.antiderivative()} + C$"

    return question, answer

def generate_definite_integral():
    a = random.randint(-5, 5)
    b = random.randint(max(-5, a), 20)

    # Build polynomial string
    polynomial = generate_polynomial()

    question = f"Calculate the following definite integral:\n\\[\\int_{{{a}}}^{{{b}}} ({polynomial})\\,dx\\]"
    answer = polynomial.antiderivative().evaluate(b) - polynomial.antiderivative().evaluate(a)

    return question, answer

def generate_polynomial_derivative():

    polynomial = generate_polynomial()

    question = f"Calculate the derivative of the following polynomial:\n \\[ p(x) = {polynomial} \\]"
    answer = f"\\[p'(x) = {polynomial.derivative()} \\]"

    return question, answer

def generate_exponential_derivative():

    coeff = generate_polynomial(2)
    exponent = generate_polynomial(1)

    exp_function = fn.Exponential(coeff, exponent)

    question = f"Calculate the derivative of the following function:\n \\[ f(x) = {exp_function} \\]"
    answer = f"\\[ f'(x) = {exp_function.derivative()}\\]"

    return question, answer

def generate_exponential_antiderivative():

    exponent = generate_polynomial(2)
    const = random.randint(2, 6)

    exp_function = fn.Exponential(fn.Polynomial([Fraction(const)]) * exponent.derivative(), exponent)
    antiderivative = fn.Exponential(fn.Polynomial([Fraction(const)]), exponent)

    question = f"Calculate the following antiderivative: $$\\int {exp_function}\\,dx$$"
    answer = f"\\[ {antiderivative}\\]"

    return question, answer

def generate_trig_derivative():
    num = random.randint(1, 6)
    if num == 1:
        function_name = r"\sin"
    elif num == 2:
        function_name = r"\cos"
    elif num == 3:
        function_name = r"\tan"
    elif num == 4:
        function_name = r"\cot"
    elif num == 5:
        function_name = r"\sec"
    elif num == 6:
        function_name = r"\csc"

    coefficient = generate_polynomial(2)
    argument = generate_polynomial(2)

    trig_function = fn.Trig(function_name, coefficient, argument)

    question = f"Calculate the derivative of the following function:\n \\[ f(x) = ({coefficient}) {function_name} ({argument}) \\]"
    answer = f"\\[ f'(x) = {trig_function.derivative()}\\]"

    return question, answer    