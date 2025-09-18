#Simple portifolio risk calculator which calculates total value and expected potential risk.
import csv
import os

def load_portfolio(file_path):
    portfolio = []
    with open(file_path, mode='r') as file:
        csv_reader = csv.DictReader(file)
        for row in csv_reader:
            portfolio.append({
                'asset': row['asset'],
                'value': float(row['value']),
                'risk': float(row['risk'])
            })
    return portfolio
def calculate_total_value(portfolio): 
    total_value = 0
    total_value = sum(item['value'] for item in portfolio)
    return total_value
def calculate_total_risk(portfolio):
    total_risk = 0
    for item in portfolio:
        total_risk += item['value'] * item['risk']
    return total_risk
if __name__=="__main__":
    print("Welcome to the simple portfolio risk calculator!")
    my_portfolio = load_portfolio(r'C:\Users\jyoth\OneDrive\Desktop\DOCS\PYTHON\Riskportfolio\portfolio.csv')
    print(my_portfolio)
    total_value = calculate_total_value(my_portfolio)
    total_risk = calculate_total_risk(my_portfolio)
    print(f"Total Portfolio Value: ${total_value:,.2f}")
    print(f"Expected Potential Risk: ${total_risk:,.2f}")