"""
CP1404/CP5632 Practical
Cumulative Total Income Program
"""

def main():
    """Get monthly incomes and display an income report."""
    incomes = []
    num_months = int(input("How many months? "))

    for month in range(1, num_months + 1):
        income = float(input(f"Enter income for month {month}: "))  # Using f-string
        incomes.append(income)

    print_income_report(incomes, num_months)


def print_income_report(incomes, num_months):
    """Print income report showing month-wise income and cumulative total."""
    print("\nIncome Report\n-------------")
    total = 0
    for month in range(1, num_months + 1):
        income = incomes[month - 1]
        total += income
        print(f"Month {month:2} - Income: ${income:10.2f} Total: ${total:10.2f}")

        
main()