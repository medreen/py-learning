basic_salary = float(input('Enter basic salary: '))
benefits = float(input('Enter benefits: '))

def get_gross(basic_salary, benefits):
    return basic_salary + benefits

def get_nhif(gross_salary):
    if gross_salary <= 5999:
        return 150
    elif gross_salary <= 7999:
        return 300
    elif gross_salary <= 11999:
        return 400
    elif gross_salary <= 14999:
        return 500
    elif gross_salary <= 19999:
        return 600
    elif gross_salary <= 24999:
        return 750
    elif gross_salary <= 29999:
        return 850
    elif gross_salary <= 34999:
        return 900
    elif gross_salary <= 39999:
        return 950
    elif gross_salary <= 44999:
        return 1000
    elif gross_salary <= 49999:
        return 1100
    elif gross_salary <= 59999:
        return 1200
    elif gross_salary <= 69999:
        return 1300
    elif gross_salary <= 79999:
        return 1400
    elif gross_salary <= 89999:
        return 1500
    elif gross_salary <= 99999:
        return 1600
    else:
        return 1700

def get_nssf(gross_salary):
    # Assuming standard 6% rate capped at 1080 for Kenya Tier II
    return min(gross_salary * 0.06, 1080)

def get_nhdf(gross_salary):
    return gross_salary * 0.015

def get_taxable_income(gross_salary, nssf, nhdf, nhif):
    return gross_salary - (nssf + nhdf + nhif)

def get_payee(taxable_income):
    relief = 2400
    if taxable_income <= 24000:
        paye = taxable_income * 0.1
    elif taxable_income <= 32333:
        paye = (24000 * 0.1) + (taxable_income - 24000) * 0.25
    else:
        paye = (24000 * 0.1) + (8333 * 0.25) + (taxable_income - 32333) * 0.30

    return max(paye - relief, 0)

def get_net_salary(gross, nhif, nssf, nhdf, payee):
    return gross - (nhif + nssf + nhdf + payee)

gross = get_gross(basic_salary, benefits)
nhif = get_nhif(gross)
nssf = get_nssf(gross)
nhdf = get_nhdf(gross)
taxable_income = get_taxable_income(gross, nssf, nhdf, nhif)
payee = get_payee(taxable_income)
net_salary = get_net_salary(gross, nhif, nssf, nhdf, payee)

print("\n--- Salary Breakdown ---")
print("Gross Salary:", gross)
print("NHIF:", nhif)
print("NSSF:", nssf)
print("NHDF:", nhdf)
print("Taxable Income:", taxable_income)
print("PAYE:", payee)
print("Net Salary:", net_salary)
