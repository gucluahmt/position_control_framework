import pandas as pd
import numpy as np
from faker import Faker
import random

# Initialize Faker and random seed for consistency
fake = Faker()
np.random.seed(42)

# Number of trades to generate
n = 1000  # You can scale this to 10_000 if needed

# Sample stock symbols and trade side
symbols = ['AAPL', 'GOOGL', 'MSFT', 'TSLA', 'AMZN', 'NVDA']
sides = ['Buy', 'Sell']

# Generate synthetic trade records
records = []

for i in range(n):
    trade_id = f'TR-{i+1:05d}'
    symbol = random.choice(symbols)
    quantity = random.randint(10, 1000)
    execution_price = round(random.uniform(100, 1000), 2)
    market_price = round(execution_price * random.uniform(0.95, 1.05), 2)
    side = random.choice(sides)
    execution_time = fake.date_time_between(start_date='-30d', end_date='now')

    # Calculate P&L based on trade side
    if side == 'Buy':
        pnl = round((market_price - execution_price) * quantity, 2)
    else:
        pnl = round((execution_price - market_price) * quantity, 2)

    # Append trade record
    records.append([
        trade_id, symbol, quantity, execution_price,
        market_price, side, execution_time, pnl
    ])

# Create DataFrame
columns = ['trade_id', 'symbol', 'quantity', 'execution_price', 'market_price', 'side', 'execution_time', 'pnl']
df = pd.DataFrame(records, columns=columns)

# Export to CSV file
df.to_csv("trading_data.csv", index=False)

print("✅ CSV file successfully created: trading_data.csv")
