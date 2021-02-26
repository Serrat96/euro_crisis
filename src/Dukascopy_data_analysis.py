import pandas as pd
import os

currencies_list = os.listdir(".\DUKASCOPY_EUR_4H_BID")

print("The available data are: ")

for i in currencies_list:

    print(i)

print("\n")

EUR_AUD = pd.read_csv(".\DUKASCOPY_EUR_4H_BID\EURAUD_Candlestick_4_h_BID_07.10.2005-20.02.2021.csv")

print(EUR_AUD.head())

print(EUR_AUD.columns)

columnas = EUR_AUD.columns