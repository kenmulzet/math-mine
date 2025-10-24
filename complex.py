import cmath

z = 3 + 4j
print(z.real)
print(z.imag)

a = 2 + 3j
b = 1 - 4j

print(a + b)     # (3 - 1j)
print(a * b)     # (14 - 5j)
print(a.conjugate())  # (2 - 3j)
print(a ** 2 * b ** 3)

root = cmath.sqrt(a)

rounded_root = complex(round(root.real, 3), round(root.imag, 3))
print(rounded_root)  # Output: (2+1j)

print(abs(a))
print(cmath.phase(a))

r, theta = cmath.polar(a)
print(f"Magnitude: {r}, Argument: {theta}")

