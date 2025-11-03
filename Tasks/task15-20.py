basic_salary = float(input('Enter basic salary: '))
benefits = float(input('Enter benefits: '))
gross_salary = basic_salary + benefits
nhif = 0
nssf = 0

if gross_salary <= 5999:
    nhif += 150
elif gross_salary <= 7999 and gross_salary >= 6000:
    nhif += 300
elif gross_salary <= 11999 and gross_salary >= 8000:
    nhif += 400
elif gross_salary <= 14999 and gross_salary >= 12000 :
    nhif += 500
elif gross_salary <= 19999 and gross_salary >= 15000:
    nhif += 600
elif gross_salary <= 24999 and gross_salary >= 20000:
    nhif += 750
elif gross_salary <= 29999 and gross_salary >= 25000:
    nhif += 850
elif gross_salary <= 34999 and gross_salary >= 30000:
    nhif += 900
elif gross_salary <= 39999 and gross_salary >= 35000:
    nhif += 950
elif gross_salary <= 44999 and gross_salary >= 40000:
    nhif += 1000
elif gross_salary <= 49999 and gross_salary >= 45000:
    nhif += 1100   
elif gross_salary <= 59999 and gross_salary >= 50000:
    nhif += 1200
elif gross_salary <= 69999 and gross_salary >= 60000:
    nhif += 1300
elif gross_salary <= 79999 and gross_salary >= 70000:
    nhif += 1400
elif gross_salary <= 89999 and gross_salary >= 80000:
    nhif += 1500
elif gross_salary <= 99999 and gross_salary >= 90000:
    nhif += 1600
elif gross_salary >= 100000:
    nhif += 1700

#16
if gross_salary >= 18000:
    nssf +=  (6/100) * gross_salary
else:
    nssf += 0

#17
nhdf = gross_salary * 0.015

#18
taxable_income = gross_salary - (nssf + nhdf + nhif)

#19
total_paye = 0
relief = 2400

if taxable_income >= 24000:
    total_paye += 0.1 * 24000
elif taxable_income >= (24000 + 8333):
    total_paye += 0.25 * 8333
elif taxable_income >= (24000 + 8333 + 467667):
    total_paye += 0.3 * 467667
elif taxable_income >= (24000 + 8333 + 467667 + 300000):
    total_paye += 0.325 * 300000
elif taxable_income >= 800000:
    total_paye += 0.35 * 800000
else:
    total_paye = 0

payee = total_paye - relief
net_salary = gross_salary - (nhif + nhdf +  nssf + payee)

print(f'Gross Salary: {gross_salary}')
print(f'NHIF: {nhif}')
print(f'NHDF: {nhdf}')
print(f'NSSF: {nssf}')
print(f'PAYE: {payee}')
print(f'Net Salary: {net_salary}')





