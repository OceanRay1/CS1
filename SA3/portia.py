# Author: Roshan Shivnani
# Date: 09/25/2026
# Purpose/Description: Compare Worth: Problem 2
# File: portia.py
# Course: CS1

#Initial values for variables
BRUTUS_INITIAL_DEPOSIT = 1
PORTIA_INITIAL_DEPOSIT = 100000
BRUTUS_INTEREST_RATE = 1.05
PORTIA_INTEREST_RATE = 1.04

#Computes Brutus's and Portia's balance each year until Brutus's worth exceeds Portia's
def Wealth(brutus_wealth, portia_wealth):
    Year = 0
    while brutus_wealth < portia_wealth:
        brutus_wealth = brutus_wealth * BRUTUS_INTEREST_RATE
        portia_wealth = portia_wealth * PORTIA_INTEREST_RATE
        Year += 1

    #Prints the year Brutus has more money than Portia and their respective interest earned
    print("Brutus's balance exceeds Portia's in year " + str(year))
    print("The interest earned by Brutus's account is " + str(brutus_wealth - 1))
    print("The interest earned by Brutus's account is " + str(portia_wealth - 1))

Wealth(BRUTUS_INITIAL_DEPOSIT, PORTIA_INITIAL_DEPOSIT)