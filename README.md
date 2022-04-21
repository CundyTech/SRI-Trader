# SRI-Trader
Stock trader that uses the Relative Strength Index (RSI) indicator to decide to buy, sell or hodl any given stock.

# Example

**Ticker** : TSLA


|Period|Ticker|Action
| ------------- | ------------- |------------- |
| 2022-04-21 11:35:00-04:00  |  TSLA  |  Buy  |
| 2022-04-21 11:35:00-04:00  |  TSLA  |  Hodl  |
| 2022-04-21 11:40:09-04:00  |  TSLA  |  Sell  |

# TODO

1. Add trader module giving the ability to buy and sell based on suggested action
2. Add unit tests which test accuracy of suggestions

# References

This project is based off infomation found here:
https://www.alpharithms.com/relative-strength-index-rsi-in-python-470209/
