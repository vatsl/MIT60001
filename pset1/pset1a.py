# -*- coding: utf-8 -*-
"""
Created on Fri Jun 30 14:27:10 2017

@author: coldKnight
"""

"""
Part A
"""
annual_salary = float(input("Enter your annual salary: "))
portion_saved = float(input("Enter the percentage of your salary to save, as decimal: "))
total_cost = float(input("Enter the cost of your dream home: "))

portion_down_payment = 0.25
rate_of_return = 0.04
current_savings = 0

monthly_salary = annual_salary/12.0
monthly_saving = monthly_salary * portion_saved

epsilon = 0.1
target_savings = total_cost * portion_down_payment

#print("target_savings: ", target_savings)

num_months = 0

while(abs(target_savings - current_savings) >= epsilon and current_savings < target_savings):
    current_savings *= (1+ (rate_of_return/12.0))
    current_savings += monthly_saving
    num_months += 1
    #print("current_savings: ", current_savings)
    
print('Number of months: ', num_months)