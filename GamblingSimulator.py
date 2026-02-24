# GamblingSimulator.py

import random

def run_simulation(stake, goal, trials):
    wins = 0
    total_bets = 0

    for _ in range(trials):
        cash = stake
        bets = 0

        while cash > 0 and cash < goal:
            bets += 1
            # Fair bet: 50% chance to win or lose
            if random.random() < 0.5:
                cash += 1
            else:
                cash -= 1

        if cash == goal:
            wins += 1

        total_bets += bets

    win_percent = (wins / trials) * 100
    avg_bets = total_bets / trials

    return wins, win_percent, avg_bets

def main():
    try:
        stake = int(input("Enter initial stake (INR): "))
        goal = int(input("Enter goal amount (INR): "))
        trials = int(input("Enter number of trials: "))

        if stake <= 0 or goal <= 0 or trials <= 0:
            raise ValueError("All inputs must be positive integers.")

        wins, win_percent, avg_bets = run_simulation(stake, goal, trials)

        print("\n--- Gambling Simulation Results ---")
        print(f"Number of times won: {wins}")
        print(f"Percent of games won: {win_percent:.2f}%")
        print(f"Average number of bets: {avg_bets:.2f}")

    except ValueError as e:
        print("Input Error:", e)

if __name__ == "__main__":
    main()
