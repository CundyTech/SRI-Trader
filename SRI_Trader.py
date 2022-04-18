import pandas as pd
import pandas_ta as ta
import GetData as gd

# https://www.alpharithms.com/relative-strength-index-rsi-in-python-470209/

l = 14

dataSet = gd.GetData('BTC-USD', '1d', '5m')

# Calculate the RSI via pandas_ta
dataSet.ta.rsi(
    close='Close',
    length=l,
    append=True, 
    signal_indicators=True, 
    xa=60, 
    xb=40)

pd.set_option('display.max_rows', None)
pd.set_option('display.max_columns', None)
pd.set_option('display.width', None)
pd.set_option('display.max_colwidth', None)

# View the result
#print(dataSet)

# Buy or Sell?
last_row = dataSet.iloc[-1]

print(last_row)

if last_row[6] == 1:
  print("Buy")
elif last_row[7] == 1:
  print("Sell")
else:
  print("Do Nothing")