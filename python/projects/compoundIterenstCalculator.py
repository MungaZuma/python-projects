# compound interest formula

# A = P (1 + r/n)**(nt)

# A = the future value of the investment/loan, including interest
# P = the principal investment amount (the initial deposit or loan amount)
# r = the annual interest rate (decimal)
# n = the number of times that interest is compounded per unit t
# t = the time the money is invested or borrowed for

import math as math


def compoundInterest(principal,rate,numberOfCompounds,time):
    compoundedAmount = principal * pow((1 + rate/numberOfCompounds), numberOfCompounds * time)

    return compoundedAmount


compoundedAmount = float(0)
principal = float(input ("enter your principle amount: "))
rate = float(input("enter the compounding rate: "))
numberOfCompounds = int(input("enter the rate of componding. 1,2,4,12,365 for annually, semi-annually, quaterly, monthly and daily respectively: "))
time = float(input("enter duration in years: "))


print("total = ", format(round(compoundInterest(principal,rate,numberOfCompounds,time))))