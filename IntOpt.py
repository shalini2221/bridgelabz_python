def main():
    # Taking input values
    a = user_input_int()
    b = user_input_int()
    c = user_input_int()

    # Integer operations
    result1 = a + b * c       # b * c first, then added to a
    result2 = a * b + c       # a * b first, then added to c
    result3 = c + a / b       # a / b first, then added to c (note: division gives float)
    result4 = a % b + c       # a % b first, then added to c

    # Printing results
    print("a + b * c =", result1)
    print("a * b + c =", result2)
    print("c + a / b =", result3)
    print("a % b + c =", result4)

if __name__ == "__main__":
    main()
