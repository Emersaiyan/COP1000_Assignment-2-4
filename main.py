# input statements
salary = 60000
numDependents = 3

# calculate taxes here
stateTax = salary * 0.065
federalTax = salary * 0.28
dependentDeduction = salary * (numDependents * 0.025)
totalWithholding = stateTax + federalTax + dependentDeduction
takeHomePay = salary - totalWithholding

# output statements
print("State withholding tax: $" + str(stateTax))
print("Federal withholding tax: $" + str(federalTax))
print("Dependent deductions: $" + str(dependentDeduction))
print("Salary: $" + str(salary))
print("Take Home Pay: $" + str(takeHomePay))
