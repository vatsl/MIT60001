# -*- coding: utf-8 -*-
"""
Created on Fri Jun 30 14:27:10 2017

@author: coldKnight
"""
    
"""
Part B
"""
annual_salary = float(input("Enter your annual salary: "))
portion_saved = float(input("Enter the percentage of your salary to save, as decimal: "))
total_cost = float(input("Enter the cost of your dream home: "))
semi_annual_raise = float(input("Enter the semi-annual raise, as a decimal: "))

portion_down_payment = 0.25
rate_of_return = 0.04
current_savings = 0

monthly_salary = annual_salary/12.0

epsilon = 0.1
target_savings = total_cost * portion_down_payment

#print("target_savings: ", target_savings)

num_months = 0

while(abs(target_savings - current_savings) >= epsilon and current_savings < target_savings):    
    num_months += 1
    current_savings *= (1+ (rate_of_return/12.0))
    
    if((num_months) % 6 == 0):
        monthly_salary *= (1 + semi_annual_raise)
        #print('raise in month: ', num_months)
        
    monthly_saving = monthly_salary * portion_saved
    current_savings += monthly_saving
    
    #print("current_savings: ", current_savings)
    
print('Number of months: ', num_months)