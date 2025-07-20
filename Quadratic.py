import sys
import math

# Check if correct number of arguments is given
if len(sys.argv) != 4:
    print("Usage: python Quadratic.py <a> <b> <c>")
    sys.exit(1)

# Read input values from command line
a = float(sys.argv[1])
b = float(sys.argv[2])
c = float(sys.argv[3])

# Check if 'a' is zero (not a quadratic equation)
if a == 0:
    print("Coefficient 'a' cannot be zero for a quadratic equation.")
    sys.exit(1)

# Calculate discriminant (delta)
delta = b * b - 4 * a * c

# Check nature of roots
if delta < 0:
    print("No real roots.")
else:
    root1 = (-b + math.sqrt(delta)) / (2 * a)
    root2 = (-b - math.sqrt(delta)) / (2 * a)
    print("Root 1:", root1)
    print("Root 2:", root2)
