#Prompting user to enter their financial details
Monthly_income = int(input("Enter your monthly income : "))
Monthly_expenses = int(input("Enter your total monthly expenses:"))

#calculating monthly savings
Monthly_savings = Monthly_income - Monthly_expenses
 
interest_rate = 0.05 

Projected_savings = Monthly_savings * 12 + (Monthly_savings*12*interest_rate)

print(f"Your monthly savings are: {Monthly_savings}")
print(f"Projected savings after one year, with interest , is : {Projected_savings}")
