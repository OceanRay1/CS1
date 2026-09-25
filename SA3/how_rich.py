# Author: Roshan Shivnani
# Date: 09/25/2026
# Purpose/Description: Wealth Calculation: Problem 1
# File: how_rich.py
# Course: CS1

#Initial values for variables
BRUTUS_INITIAL_DEPOSIT = 1
BRUTUS_INTEREST_RATE = 1.05
TOTAL_YEARS = 2023

#Takes Brutus's starting wealth and computes worth 2023 years later at 5% interest
def Wealth(brutus_wealth):
    for year in range(TOTAL_YEARS):
        brutus_wealth = brutus_wealth * BRUTUS_INTEREST_RATE
    return brutus_wealth

print("At year 2, the balance is " + str(Wealth(BRUTUS_INITIAL_DEPOSIT)))
print("At year 2, the interest is " + str(Wealth(BRUTUS_INITIAL_DEPOSIT) - 1))