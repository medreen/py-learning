basic_salary = float(input('Enter basic salary: '))
benefits = float(input('Enter benefits: '))

def get_gross(basic_salary, benefits):
    return basic_salary + benefits

def get_nhif(gross_salary):
    if gross_salary >0 and gross_salary <= 5999:
        nhif = 150
    elif gross_salary <= 7999 and gross_salary >= 6000:
        nhif = 300
    elif gross_salary <= 11999 and gross_salary >= 8000:
        nhif = 400
    elif gross_salary <= 14999 and gross_salary >= 12000 :
        nhif = 500
    elif gross_salary <= 19999 and gross_salary >= 15000:
        nhif = 600
    elif gross_salary <= 24999 and gross_salary >= 20000:
        nhif = 750
    elif gross_salary <= 29999 and gross_salary >= 25000:
        nhif = 850
    elif gross_salary <= 34999 and gross_salary >= 30000:
        nhif = 900
    elif gross_salary <= 39999 and gross_salary >= 35000:
        nhif = 950
    elif gross_salary <= 44999 and gross_salary >= 40000:
        nhif = 1000
    elif gross_salary <= 49999 and gross_salary >= 45000:
        nhif = 1100   
    elif gross_salary <= 59999 and gross_salary >= 50000:
        nhif = 1200
    elif gross_salary <= 69999 and gross_salary >= 60000:
        nhif = 1300
    elif gross_salary <= 79999 and gross_salary >= 70000:
        nhif = 1400
    elif gross_salary <= 89999 and gross_salary >= 80000:
        nhif = 1500
    elif gross_salary <= 99999 and gross_salary >= 90000:
        nhif = 1600
    elif gross_salary >= 100000:
        nhif = 1700

    return nhif

def get_nssf(gross_salary):
    if gross_salary < 18000:
        nssf = 18000 * 0.6
    else:
        nssf = 1080
    return nssf

def get_nhdf(gross_salary):
    return gross_salary * 0.015

def get_taxable_income(gross_salary, nssf, nhdf, nhif):
    return gross_salary - (nssf + nhdf + nhif)

def get_payee(taxable_income):
    relief = 2400
    if taxable_income >= 0 and taxable_income <= 24000:
        paye = taxable_income * 0.1
    elif taxable_income >24000 and  taxable_income <= 32333:
        paye = (24000 * 0.1) + (taxable_income - 24000) * 0.25
    elif taxable_income >= 32333 and taxable_income <= 500000:
        paye = (24000 * 0.1) + (8333 * 0.25) + (taxable_income - 32333) * 0.30
    elif taxable_income >= 500000 and  taxable_income <= 800000: #24000 + 8333 + 467467 + 300000
        paye = 24000 * 0.1 + 8333 * 0.25 + 467667 * 0.3 + (taxable_income - 500000) * 0.325
    else: #24000 + 8333 + 467467 + 300000 + 800000
        paye = paye = 24000 * 0.1 + 8333 * 0.25 + 467667 * 0.3 + taxable_income - 800000 * 0.35
    payee = paye - relief

    return payee

def get_net_salary(gross, nhif, nssf, nhdf, paye):
    return gross - (nhif + nssf + nhdf + payee)

#function calls    
gross_salary = get_gross(basic_salary, benefits)
nhif = get_nhif(gross_salary)
nssf = get_nssf(gross_salary)
nhdf = get_nhdf(gross_salary)
taxable_income = get_taxable_income(gross_salary, nssf, nhdf, nhif)
payee = get_payee(taxable_income)
net_sal = get_net_salary(gross_salary, nhif, nssf, nhdf, payee)

print("-----------------------------Income Tax-------------------------------")
print(f'Gross Salary is {gross_salary}')
print(f'NHIF: KSH. {nhif}')
print(f'NSSF: KSH> {nssf}')
print(f'NHDF: KSH. {nhdf}')
print(f'Taxaable Income: KSH. {taxable_income}')
print(f'Payee: KSH. {payee}')
print(f'Net Salary: KSH. {net_sal}')
print("----------------------------------------------------------------------")


