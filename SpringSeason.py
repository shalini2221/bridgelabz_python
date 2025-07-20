import sys

# Check if enough command-line arguments are provided
if len(sys.argv) != 3:
    print("Usage: python SpringSeason.py <month> <day>")
    sys.exit(1)

# Read command-line arguments
m = int(sys.argv[1])
d = int(sys.argv[2])

# Determine if the date is in the spring season (March 20 to June 20)
if (m == 3 and d >= 20) or (m == 4) or (m == 5) or (m == 6 and d <= 20):
    print("true")
else:
    print("false")
