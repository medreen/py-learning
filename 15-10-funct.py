basic_salary = float(input('Enter basic salary: '))
benefits = float(input('Enter benefits: '))

def get_gross(basic_salary, benefits):
    return basic_salary + benefits

gross_salary = get_gross(basic_salary, benefits)
print(gross_salary)

def get_nhif(gross_salary):
    if gross_salary <= 5999:
        nhif = 150
    elif gross_salary <= 7999:
        nhif = 300
    elif gross_salary <= 11999:
        nhif = 400
    elif gross_salary <= 14999:
        nhif = 500
    elif gross_salary <= 19999:
        nhif = 600
    elif gross_salary <= 24999:
        nhif = 750
    elif gross_salary <= 29999:
        nhif = 850
    elif gross_salary <= 34999:
        nhif = 900
    elif gross_salary <= 39999:
        nhif = 950
    elif gross_salary <= 44999:
        nhif = 1000
    elif gross_salary <= 49999:
        nhif = 1100
    elif gross_salary <= 59999:
        nhif = 1200
    elif gross_salary <= 69999:
        nhif = 1300
    elif gross_salary <= 79999:
        nhif = 1400
    elif gross_salary <= 89999:
        nhif = 1500
    elif gross_salary <= 99999:
        nhif = 1600
    else:
        nhif = 1700
return nhif

nhif = get_nhif(gross_salary)
print(nhif)


def get_nssf(gross_salary):
    if gross_salary < 18000:
        nssf = 18000 * 0.6
    else:
        nssf = 1080
    return nssf

nssf = get_nssf(gross_salary)
print(nssf)


def get_nhdf(gross_salary):
    return gross_salary * 0.015

nhdf = get_nhdf(gross_salary)
print(nhdf)

def get_taxable_income(gross_salary, nssf, nhdf, nhif):
    return gross_salary - (nssf + nhdf + nhif)

taxable_income = get_taxable_income(gross_salary, nssf, nhdf, nhif)
print(taxable_income)

def get_payee(taxable_income):
    relief = 2400
    if taxable_income <= 24000:
        paye = taxable_income * 0.1
    elif taxable_income <= 32333:
        paye = (24000 * 0.1) + (taxable_income - 24000) * 0.25
    elif taxable_income <= 500000:
        paye = (24000 * 0.1) + (8333 * 0.25) + (taxable_income - 32333) * 0.30
    elif taxable_income <= 800000: #24000 + 8333 + 467467 + 300000
        paye = 24000 * 0.1 + 8333 * 0.25 + 467667 * 0.3 + (taxable_income - 500000) * 0.325
    else: #24000 + 8333 + 467467 + 300000 + 800000
        paye = paye = 24000 * 0.1 + 8333 * 0.25 + 467667 * 0.3 + taxable_income - 800000 * 0.35

    return paye - relief, 0

paye = get_payee(taxable_income)
print(paye)

def get_net_salary(gross, nhif, nssf, nhdf, payee):
    return gross - (nhif + nssf + nhdf + payee)


