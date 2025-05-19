import pandas as pd
import pyodbc


df = pd.read_csv('/Users/ahmetguclu/Desktop/trading_data.csv')


conn = pyodbc.connect(
    'DRIVER={ODBC Driver 17 for SQL Server};SERVER=localhost,1433;DATABASE=master;UID=sa;PWD=Str0ng@Passw0rd'
)
cursor = conn.cursor()


for index, row in df.iterrows():
    cursor.execute("""
        INSERT INTO trading_data (trade_id, symbol, quantity, execution_price, market_price, side, execution_time, pnl)
        VALUES (?, ?, ?, ?, ?, ?, ?, ?)
    """, row.trade_id, row.symbol, row.quantity, row.execution_price, row.market_price, row.side, row.execution_time, row.pnl)

conn.commit()
cursor.close()
conn.close()
