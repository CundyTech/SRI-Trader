import pandas as pd
import pandas_ta as ta
import GetData as gd
from tabulate import tabulate


# Based on information found here: https://www.alpharithms.com/relative-strength-index-rsi-in-python-470209/

ticker = input("Enter ticker or leave blank for 'BTC-USD'):")

if ticker == "":
    ticker = 'BTC-USD' 

dataSet = gd.GetData(ticker, '1d', '5m')

# Calculate the RSI
dataSet.ta.rsi(
    close='Close',
    length=14,
    append=True, 
    signal_indicators=True, 
    xa=60, 
    xb=40)

# Get Python to show all rows when using print
pd.set_option('display.max_rows', None)
pd.set_option('display.max_columns', None)
pd.set_option('display.width', None)
pd.set_option('display.max_colwidth', None)

# View the result
#print(dataSet)

table = [['Period', 'Ticket', 'Action']]

# Calulate action (buy, sell or hodl)

last_row = dataSet.iloc[-1]
#print(last_row)

for row in dataSet.iloc:
    if row[6] == 1:
      table.append([row.T.name,ticker, 'Buy'])
    elif row[7] == 1:
      table.append([row.T.name,ticker,'Sell'])
    else:
      table.append([row.T.name,ticker,'Hodl'])

print(tabulate(table))

