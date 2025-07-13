def main():
    # Taking float (double-like) input values
    a = user_input_double()
    b = user_input_double()
    c = user_input_double()

    # Floating-point operations
    result1 = a + b * c       # b * c first, then added to a
    result2 = a * b + c       # a * b first, then added to c
    result3 = c + a / b       # a / b first, then added to c
    result4 = a % b + c       # a % b first, then added to c

    # Printing results
    print("a + b * c = ", result1)
    print("a * b + c = ", result2)
    print("c + a / b = ", result3)
    print("a % b + c = ", result4)

if __name__ == "__main__":
    main()
