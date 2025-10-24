import random

def generate_linear_equation(latex = False):
    a = random.randint(1, 50)
    b = random.randint(-50, 50)
    x = random.randint(-25, 25)

    if latex: latex_sym = "$$" 
    else: latex_sym = ""

    if a == 1:
        coeff = ""
    else:
        coeff = str(a)
    if (b > 0):
        question = f"Solve for x: {latex_sym}{coeff}x + {b} = {a * x + b}{latex_sym}"
    elif (b == 0):
        question = f"Solve for x: {latex_sym}{coeff}x = {a * x}{latex_sym}"
    elif (b < 0):
        question = f"Solve for x: {latex_sym}{coeff}x - {abs(b)} = {a * x + b}{latex_sym}"
    answer = f"{latex_sym}x = {x}{latex_sym}"
    return question, answer

def generate_quadratic_polynomial():
    # generates a factorable quadratic polynomial
    # and returns the polynomial and its roots
    a = random.randint(1, 20)
    b = random.randint(-20, 20)

    sum_ab = a + b
    prod_ab = a*b

    if sum_ab < 0:
        sign_x = "+"
    elif sum_ab > 0:
        sign_x = "-"
    if prod_ab < 0:
        sign_ab = "-"
    elif prod_ab > 0:
        sign_ab = "+"

    if sum_ab == 0:
        if a != 0:
            expression = f"x² - {abs(prod_ab)}"
        else:
            expression = f"x²"
    elif b == 0:
        if abs(a) == 1:
            expression = f"x² {sign_x} x"
        else:
            expression = f"x² {sign_x} {a}x"
    else:
        if abs(sum_ab) == 1:
            expression = f"x² {sign_x} x {sign_ab} {abs(prod_ab)}"
        else:
            expression = f"x² {sign_x} {abs(sum_ab)}x {sign_ab} {abs(prod_ab)}"

    return expression, a, b

def format_root(r):
    return f"(x - {r})" if r > 0 else f"(x + {-r})" if r < 0 else "x"

def generate_factor_quadratic():
    expression, r1, r2 = generate_quadratic_polynomial()
    question = f"Factor the following polynomial: {expression}"
    answer = f"{format_root(r1)}{format_root(r2)}"
    return question, answer

def generate_quadratic_equation():
    # generates a quadratic equation with integer roots
    polynomial, r1, r2 = generate_quadratic_polynomial()
    question = f"Solve for x: {polynomial} = 0"
    answer = f"x = {r1}, {r2}"
    return question, answer
