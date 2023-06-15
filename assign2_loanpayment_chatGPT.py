# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

def calculate_monthly_repayment(PV, r, n):
    monthly_interest_rate = r / 12
    denominator = 1 - (1 + monthly_interest_rate) ** -n
    monthly_payment = monthly_interest_rate * PV / denominator
    return monthly_payment

# Taking user input
PV = float(input("Enter the Present Value (PV): "))
r = float(input("Enter the Annual Percentage Rate (r): "))
n = int(input("Enter the number of months (n): "))

monthly_repayment = calculate_monthly_repayment(PV, r, n)
print("Monthly Repayment Amount:", monthly_repayment)

50
