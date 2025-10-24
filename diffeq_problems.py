import random
import functions as fn
from fractions import Fraction

def generate_difference_eqn():
    a1 = random.randint(1, 5)
    a2 = random.randint(1, 5)
    a = random.randint(1, 10)
    b = a

    while (b == a) or (b == -a) or (b == 0):
        b = random.randint(-10, 10)

    sign = "+"
    if b * a > 0:
        sign = "-"

    question = f"Determine an explicit formula for $a_n$ if $a_1 = {a1}, a_2 = {a2}$, and $$a_n = {a + b} a_{{n - 1}} {sign} {abs(a*b)} a_{{n - 2}}$$"
    coeff1 = Fraction((a1*b^2 - a2*b)/(a*b^2-b*a^2))
    coeff2 = Fraction((a*a2-a1*a^2)/(a*b^2-b*a^2))

    answer = f"$a_n = {coeff1} * {a}^n + {coeff2} * {b}^n$"

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
    answer = f"\\[ y = c_1 e^" + "{" + f"{a}x" + "} + c_2 e^" + "{" + f"{b}x" + "} \\]"

    return question, answer