#!/usr/bin/env python3

# finance_calculator.py

# Prompt the user for their financial details in Kenyan Shillings
monthly_income = float(input("Enter your monthly income: "))
monthly_expenses = float(input("Enter your total monthly expenses: "))

# Calculate monthly savings
monthly_savings = monthly_income - monthly_expenses

# Project annual savings with interest
annual_savings = monthly_savings * 12
projected_savings = annual_savings + (annual_savings * 0.05)

# Display the results
print(f"Your monthly savings are KES {monthly_savings:,.2f}.")
print(f"Projected savings after one year, with interest, is: KES {projected_savings:,.2f}.")

