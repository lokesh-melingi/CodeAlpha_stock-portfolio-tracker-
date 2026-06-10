# Stock Portfolio Tracker

# Hardcoded stock prices
stock_prices = {
    "AAPL": 180,
    "TSLA": 250,
    "GOOG": 150,
    "MSFT": 320,
    "AMZN": 140
}

portfolio = {}
total_investment = 0

print("=" * 45)
print("      STOCK PORTFOLIO TRACKER")
print("=" * 45)

# Number of stocks user wants to enter
n = int(input("How many stocks do you want to add? : "))

# Input stock details
for i in range(n):
    stock_name = input("\nEnter stock symbol: ").upper()

    if stock_name in stock_prices:
        quantity = int(input(f"Enter quantity of {stock_name}: "))

        portfolio[stock_name] = quantity
    else:
        print("Stock not available in database!")

# Calculate investment
print("\n" + "=" * 45)
print("           PORTFOLIO SUMMARY")
print("=" * 45)

for stock, quantity in portfolio.items():
    price = stock_prices[stock]
    investment = price * quantity
    total_investment += investment

    print(f"{stock} -> Price: ${price} | Quantity: {quantity} | Value: ${investment}")

print("=" * 45)
print(f"Total Investment Value = ${total_investment}")
print("=" * 45)

# Save report to text file
file = open("portfolio_report.txt", "w")

file.write("STOCK PORTFOLIO REPORT\n")
file.write("=" * 40 + "\n")

for stock, quantity in portfolio.items():
    price = stock_prices[stock]
    investment = price * quantity

    file.write(f"{stock} -> Price: ${price}, Quantity: {quantity}, Value: ${investment}\n")

file.write("=" * 40 + "\n")
file.write(f"Total Investment Value = ${total_investment}")

file.close()

print("\nPortfolio report saved successfully as 'portfolio_report.txt'")