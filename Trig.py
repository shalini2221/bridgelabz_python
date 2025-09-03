# Trig.py

import math

def main():
    try:
        angle_degrees = float(input("Enter angle in degrees: "))
        angle_radians = math.radians(angle_degrees)

        sin_val = math.sin(angle_radians)
        cos_val = math.cos(angle_radians)
        tan_val = math.tan(angle_radians)

        print(f"\nTrigonometric Calculations for {angle_degrees}°:")
        print(f"Radians: {angle_radians:.4f}")
        print(f"sin({angle_degrees}) = {sin_val:.4f}")
        print(f"cos({angle_degrees}) = {cos_val:.4f}")
        print(f"tan({angle_degrees}) = {tan_val:.4f}")

        # Check the identity: sin²(x) + cos²(x) = 1
        identity = sin_val ** 2 + cos_val ** 2
        print(f"sin² + cos² = {identity:.4f} (should be close to 1)")

    except ValueError:
        print("Invalid input. Please enter a numeric value for the angle.")

if __name__ == "__main__":
    main()
