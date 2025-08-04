import random

# Generate 5 random numbers between 0 and 1
values = [random.random() for _ in range(5)]

# Calculate average, min, and max
average = sum(values) / len(values)
minimum = min(values)
maximum = max(values)

# Print the results
print("Five random values between 0 and 1:")
for i, val in enumerate(values, 1):
    print(f"Value {i}: {val}")

print(f"\nAverage: {average}")
print(f"Minimum: {minimum}")
print(f"Maximum: {maximum}")
