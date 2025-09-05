# CarLoan.py

import sys

def calculate_monthly_payment(P, Y, R):
    n = 12 * Y               # total number of monthly payments
    r = R / (12 * 100)       # monthly interest rate

    if r == 0:
        # No interest loan
        return P / n

    # Apply the formula: payment = Pr / (1 - (1 + r)^-n)
    payment = (P * r) / (1 - (1 + r) ** -n)
    return payment

def main():
    if len(sys.argv) != 4:
        print("Usage: python CarLoan.py <P> <Y> <R>")
        return

    try:
        P = float(sys.argv[1])   # Principal
        Y = int(sys.argv[2])     # Years
        R = float(sys.argv[3])   # Annual interest rate in percent

        monthly_payment = calculate_monthly_payment(P, Y, R)
        print(f"Monthly payment: ${monthly_payment:.2f}")

    except ValueError:
        print("Error: Please enter valid numbers. P and R should be numeric, Y should be an integer.")

if __name__ == "__main__":
    main()
