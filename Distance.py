import sys
import math

# Check that exactly two arguments are provided (excluding script name)
if len(sys.argv) != 3:
    print("Usage: python Distance.py <x> <y>")
    sys.exit(1)

# Parse command-line arguments
x = int(sys.argv[1])
y = int(sys.argv[2])

# Compute the Euclidean distance using math.pow
distance = math.sqrt(math.pow(x, 2) + math.pow(y, 2))

# Print the result
print(f"Distance from ({x}, {y}) to (0, 0) is: {distance}")
