# -*- coding: utf-8 -*-
"""
Created on Fri Jun 30 14:27:10 2017

@author: coldKnight
"""

"""
Part C
"""
semi_annual_raise = 0.07
annual_rate_of_return = 0.04
portion_down_payment = 0.25
total_cost = 1000000
target_months = 36

target_savings = total_cost * portion_down_payment

annual_salary = float(input("Enter the starting salary: "))
monthly_salary = annual_salary/12.0
current_savings = 0

epsilon = 100
low_rate = 0
high_rate = 10000
guess_rate = (high_rate + low_rate)/2
num_months = 0
steps = 0

while(num_months != target_months):
    num_months = 0
    while(abs(target_savings - current_savings) >= epsilon and current_savings < target_savings):    
        num_months += 1
        current_savings *= (1+ (annual_rate_of_return/12.0))
    
        if((num_months) % 6 == 0):
            monthly_salary *= (1 + semi_annual_raise)
        
        monthly_saving = monthly_salary * (guess_rate/100.0)
        current_savings += monthly_saving
            
    if(num_months < target_months):
        high_rate = guess_rate
    else:
        low_rate = guess_rate
    
    guess_rate = (high_rate + low_rate)/2
    steps += 1
    #print('Num months: ', num_months, 'Steps: ', steps, 'GR: ', guess_rate)
    current_savings = 0
    monthly_salary = annual_salary/12.0
    
if(guess_rate/100.0 > 1):
    print('It is not possible to pay down payment in three years')
    
else:
    print('Best Saving Rate: ', guess_rate/100.0)
    print('Steps in bisection search: ', steps)