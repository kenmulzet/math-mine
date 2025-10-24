import random
import math

def generate_circumference_problem():
    r = random.randint(1, 10)
    unit = pick_unit()
    unit_r = pluralize(unit, r)
    question = f"Calculate the circumference of a circle with radius {r} {unit_r}. Round your answer to 2 decimal places."
    answer = f"Circumference = {round(2*math.pi*r,2)} {pluralize(unit, 2)}"
    return question, answer

def generate_square_perimeter_problem():
    s = random.randint(1, 10)
    unit = pick_unit()
    unit_s = pluralize(unit, s)
    question = f"Calculate the perimeter of a square with side length {s} {unit_s}."
    answer = f"Perimeter = {4*s} {pluralize(unit, 2)}"
    return question, answer

def generate_square_area_problem():
    s = random.randint(1, 10)
    unit = pick_unit()
    unit_s = pluralize(unit, s)
    question = f"Calculate the area of a square with side length {s} {unit_s}."
    area = s * s
    answer = f"Area = {area} square {unit_s}"
    return question, answer

def generate_circle_area_problem():
    r = random.randint(1, 10)
    unit = pick_unit()
    unit_r = pluralize(unit, r)
    question = f"Calculate the area of a circle with radius {r} {unit_r}. Round your answer to 2 decimal places."
    answer = f"Area = {round(math.pi*r*r,2)} square {pluralize(unit, 2)}"
    return question, answer

def generate_triangle_area_problem():
    a = random.randint(1, 10)
    b = random.randint(1, 10)
    unit = pick_unit()
    unit_a = pluralize(unit, a)
    unit_b = pluralize(unit, b)
    unit_c = pluralize(unit, 0.5 * a * b)
    question = f"Calculate the area of a triangle with base {a} {unit_a} and height {b} {unit_b}."
    answer = f"Area = {format_number(0.5 * a * b)} square {unit_c}"
    return question, answer

def generate_cube_surface_area_problem():
    s = random.randint(1, 15)
    unit = pick_unit()
    unit_s = pluralize(unit, s)
    question = f"Calculate the surface area of a cube with side length {s} {unit_s}."
    answer = f"Volume = {6*s*s} square {pluralize(unit,2)}"
    return question, answer

def generate_cylinder_surface_area_problem():
    r = random.randint(1, 10)
    h = random.randint(1, 10)
    unit = pick_unit()
    unit_r = pluralize(unit, r)
    unit_h = pluralize(unit, h)
    question = f"Calculate the surface area of a cylinder with radius {r} {unit_r} and height {h} {unit_h}. Round your answer to 2 decimal places."
    answer = f"Volume = {round(2*math.pi*r*h + 2*math.pi*r*r,2)} square {pluralize(unit, 2)}"
    return question, answer

def generate_cube_volume_problem():
    s = random.randint(1, 15)
    unit_s = pluralize(pick_unit(), s)
    question = f"Calculate the volume of a cube with side length {s} {unit_s}."
    answer = f"Volume = {s*s*s} cubic {unit_s}"
    return question, answer

def generate_cylinder_volume_problem():
    r = random.randint(1, 10)
    h = random.randint(1, 10)
    unit = pick_unit()
    unit_r = pluralize(unit, r)
    unit_h = pluralize(unit, h)
    question = f"Calculate the volume of a cylinder with radius {r} {unit_r} and height {h} {unit_h}. Round your answer to 2 decimal places."
    answer = f"Volume = {round(math.pi*r*r*h,2)} cubic {pluralize(unit, 2)}"
    return question, answer

def generate_sphere_volume_problem():
    r = random.randint(1, 10)
    unit = pick_unit()
    unit_r = pluralize(unit, r)
    question = f"Calculate the volume of a sphere with radius {r} {unit_r}. Round your answer to 2 decimal places."
    answer = f"Volume = {round(4.0*math.pi*r*r*r/3.0, 2)} cubic {pluralize(unit, 2)}"
    return question, answer

def pluralize(unit, value):
    if value > 1:
        match unit:
            case "inch": unit = "inches"
            case "foot": unit = "feet"
            case _: unit += "s"
    return unit

def pick_unit():
    u = random.randint(1, 6)
    match u:
        case 1: return "inch"
        case 2: return "foot"
        case 3: return "yard"
        case 4: return "millimeter"
        case 5: return "centimeter"
        case 6: return "meter"

def format_number(n):
    return int(n) if n == int(n) else n

#- Volume problems: Cube, cylinder, or sphere volume with unit-aware phrasing
#- Unit conversion: e.g., “Convert 12 inches to centimeters”
#- toggle whether to include the answers
#- Difficulty tiers: Let users choose between simple and compound shape