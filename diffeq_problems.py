import random
import functions as fn
from fractions import Fraction

def generate_difference_eqn():
    a1 = random.randint(1, 5)
    a2 = random.randint(1, 5)
    a = random.randint(2, 10)
    b = a

    while (abs(b) == a) or (b == 0) or (abs(b) == 1):
        b = random.randint(-10, 10)

    sign = "+"
    if b * a > 0:
        sign = "-"

    question = f"Determine an explicit formula for $a_n$ if $a_1 = {a1}, a_2 = {a2}$, and $$a_{{n + 2}} = "
    
    print(f"a = {a}, b = {b}, a1 = {a1}, a2 = {a2}")

    if a + b == 1:
        question += f"a_{{n + 1}} {sign} "
    elif a + b == -1:
        question += f"- a_{{n + 1}} {sign} "
    else:
        question += f"{a + b} \; a_{{n + 1}} {sign} "

    if abs(a*b) == 1:
        question += f"a_{{n}}$$"
    else:
        question += f"{abs(a*b)} \; a_{{n}}$$"

#    if a == b:
#        answer = "Unable to determine solution"
#    else:
#    if a != b:
    num1 = a2 - a1 * b
    den1 = a * a - a * b

    num2 = a2 - a1 * a
    den2 = b * b - a * b
    coeff1 = Fraction(num1, den1)   # exact, auto-reduced
    coeff2 = Fraction(num2, den2)   # exact, auto-reduced
#        coeff1 = Fraction((a2 - a1*b)/(a*a - a*b))
#        coeff2 = Fraction((a2 - a1*a)/(b*b - a*b))

    if coeff2 > 0:
        if a < 0 and b < 0:
            answer = f"$a_n = {coeff1} * ({a})^n + {coeff2} * ({b})^n$"
        elif a < 0:
            answer = f"$a_n = {coeff1} * ({a})^n + {coeff2} * {b}^n$"
        elif b < 0:
            answer = f"$a_n = {coeff1} * {a}^n + {coeff2} * ({b})^n$"
        else:
            answer = f"$a_n = {coeff1} * {a}^n + {coeff2} * {b}^n$"
    elif coeff2 < 0:
        if a < 0 and b < 0:
            answer = f"$a_n = {coeff1} * ({a})^n - {abs(coeff2)} * ({b})^n$"
        elif a < 0:
            answer = f"$a_n = {coeff1} * ({a})^n - {abs(coeff2)} * {b}^n$"
        elif b < 0:
            answer = f"$a_n = {coeff1} * {a}^n - {abs(coeff2)} * ({b})^n$"
        else:
            answer = f"$a_n = {coeff1} * {a}^n - {abs(coeff2)} * {b}^n$"
    elif coeff1 == 0:
        if coeff2 == 0:
            answer = f"$a_n = 0$"
        else:
            answer = f"$a_n = {coeff2} * {b}^n$"
    elif coeff2 == 0:
        answer = f"$a_n = {coeff1} * {a}^n$"

    return question, answer

def generate_second_order_eqn():
    a = random.randint(1, 10)
    b = a

    while (b == a) or (b == 0):
        b = random.randint(-10, 10)

    eqn = "\\[ y^{\\prime \\prime}"
    if (b + a < 0):
        eqn += f" - {abs(b + a)} y^{{\\prime}}"
    elif (b + a > 0):
        eqn += f" + {b + a} y^{{\\prime}}"

    if b * a > 0:
        eqn += f" + {b * a} y"
    elif b * a < 0:
        eqn += f" - {abs(b * a)} y"

    eqn += " = 0 \\]"

    question = f"Calculate the general solution to the following differential equation: {eqn}"
    answer = f"$ y = c_1 e^" + "{" + f"{a}x" + "} + c_2 e^" + "{" + f"{b}x" + "}$"

    return question, answer

def generate_bernoulli_eqn():
    a = random.randint(1, 12)
    b = a

    while (b == a) or (b == 0):
        b = random.randint(-12, 12)

    coeff1 = 1 - b - a
    coeff2 = b*a
    eqn = "\\[ x^2 y^{\\prime \\prime}"
    if (coeff1 < 0):
        eqn += f" - {abs(coeff1)} x y^{{\\prime}}"
    elif (coeff1 > 0):
        eqn += f" + {coeff1} y^{{\\prime}}"

    if coeff2 == -1:
        eqn += f" - y"
    elif coeff2 == 1:
        eqn += f" + y"
    elif coeff2 > 0:
        eqn += f" + {coeff2} y"
    elif coeff2 < 0:
        eqn += f" - {abs(coeff2)} y"

    eqn += " = 0 \\]"

    question = f"Find the general solution to the second-order Bernoulli equation: {eqn}"
    answer = f"$ y = c_1 x^{a} + c_2 x^{b}$"

    return question, answer