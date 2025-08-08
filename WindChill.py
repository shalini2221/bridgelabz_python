import sys
import math

# Check for correct number of arguments
if len(sys.argv) != 3:
    print("Usage: python WindChill.py <temperature> <wind speed>")
    sys.exit(1)

# Parse command-line arguments
t = float(sys.argv[1])  # Temperature in Fahrenheit
v = float(sys.argv[2])  # Wind speed in miles per hour

# Validate input range
if abs(t) > 50 or v <= 3:
    print("Formula is not valid for |t| > 50 or v <= 3.")
    sys.exit(1)

# Compute wind chill using the formula
wind_chill = 35.74 + 0.6215 * t + (0.4275 * t - 35.75) * math.pow(v, 0.16)

# Print result
print(f"Temperature: {t}°F")
print(f"Wind Speed: {v} mph")
print(f"Wind Chill: {wind_chill:.2f}°F")
