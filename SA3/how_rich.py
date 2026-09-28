# Author: Roshan Shivnani
# Date: 09/25/2026
# Purpose/Description: Wealth Calculation: Problem 1
# File: how_rich.py
# Course: CS1

#Initial values for variables
BRUTUS_INITIAL_DEPOSIT = 1
BRUTUS_INTEREST_RATE = 1.05
TOTAL_YEARS = 2023

#Takes starting value "brutus_wealth" and computes worth TOTAL_YEARS later at BRUTUS_INTEREST_RATE
def Wealth(brutus_wealth):
    year = 0
    while year < TOTAL_YEARS:
        brutus_wealth = brutus_wealth * BRUTUS_INTEREST_RATE
        year += 1
    return brutus_wealth

#Prints final balance and interest earned in his account
print("At the end of year 2023, the total balance is " + str(Wealth(BRUTUS_INITIAL_DEPOSIT)))
print("At the end of year 2023, the total interest earned is " + str(Wealth(BRUTUS_INITIAL_DEPOSIT) - BRUTUS_INITIAL_DEPOSIT))
