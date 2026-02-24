# Sin.py
import math

def compute_sin(x):
    x = x % (2 * math.pi)  # Normalize angle to [0, 2π)

    term = x  # First term in the series
    sin_x = 0
    n = 1

    while abs(term) > 1e-15:
        sin_x += term
        term *= -1 * x * x / ((2 * n) * (2 * n + 1))
        n += 1

    return sin_x

def main():
    try:
        x_deg = float(input("Enter angle in degrees: "))
        x_rad = math.radians(x_deg)  # Convert degrees to radians
        result = compute_sin(x_rad)
        print(f"sin({x_deg}°) ≈ {result}")
    except ValueError:
        print("Please enter a valid number.")

if __name__ == "__main__":
    main()

# Cos.py
import math

def compute_cos(x):
    x = x % (2 * math.pi)  # Normalize angle to [0, 2π)

    term = 1  # First term in the series
    cos_x = 0
    n = 0

    while abs(term) > 1e-15:
        cos_x += term
        term *= -1 * x * x / ((2 * n + 1) * (2 * n + 2))
        n += 1

    return cos_x

def main():
    try:
        x_deg = float(input("Enter angle in degrees: "))
        x_rad = math.radians(x_deg)  # Convert degrees to radians
        result = compute_cos(x_rad)
        print(f"cos({x_deg}°) ≈ {result}")
    except ValueError:
        print("Please enter a valid number.")

if __name__ == "__main__":
    main()
