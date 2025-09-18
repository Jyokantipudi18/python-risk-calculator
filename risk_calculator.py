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
                'risk': float(row['risk']),
                'sector': row['sector']
            })
    return portfolio
def calculate_diversification_score(portfolio):
    sectors = set()
    for asset in portfolio:
        sectors.add(asset['sector'])
    num_unique_sectors = len(sectors)
    total_assets = len(portfolio)
    diversification_score = num_unique_sectors / total_assets
    return diversification_score
def calculate_total_value(portfolio): 
    total_value = 0
    total_value = sum(item['value'] for item in portfolio)
    return total_value
def calculate_total_risk(portfolio):
    total_risk_value= 0
    diversification_score = calculate_diversification_score(portfolio)
    for asset in portfolio:
        # We will add a "concentration penalty" to the risk
        # This penalty increases as the diversification score goes down
        concentration_penalty = 1 / diversification_score
        individual_risk = asset['value'] * asset['risk'] * concentration_penalty
        total_risk_value += individual_risk
    return total_risk_value


    # A simple score: number of unique sectors / total number of assets
    # A score of 1.0 means every asset is in its own sector (highly diversified)
    # A score of 0.1 means all assets are in only 5 unique sectors
    diversification_score = num_unique_sectors / total_assets
    return diversification_score
if __name__=="__main__":
    print("Welcome to the simple portfolio risk calculator!")
    my_portfolio = load_portfolio(r'C:\Users\jyoth\OneDrive\Desktop\DOCS\PYTHON\Riskportfolio\portfolio.csv')
    print(my_portfolio)
    total_value = calculate_total_value(my_portfolio)
    total_risk = calculate_total_risk(my_portfolio)
    diversification_score = calculate_diversification_score(my_portfolio)
    print(f"Total Portfolio Value: ${total_value:,.2f}")
    print(f"Expected Potential Risk: ${total_risk:,.2f}")
    print(f"Diversification Score: {diversification_score:.2f}")