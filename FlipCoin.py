# FlipCoin.py
import random

def flip_coin(times):
    heads = 0
    tails = 0

    for i in range(times):
        result = random.choice(["Heads", "Tails"])
        print(f"Flip {i+1}: {result}")
        if result == "Heads":
            heads += 1
        else:
            tails += 1

    total = heads + tails
    percent_heads = (heads / total) * 100
    percent_tails = (tails / total) * 100

    print("\nFinal Results:")
    print(f"Heads: {heads} ({percent_heads:.2f}%)")
    print(f"Tails: {tails} ({percent_tails:.2f}%)")

if __name__ == "__main__":
    try:
        num_flips = int(input("Enter the number of times to flip the coin: "))
        if num_flips <= 0:
            print("Please enter a positive number.")
        else:
            flip_coin(num_flips)
    except ValueError:
        print("Invalid input. Please enter an integer.")
