import mplfinance as mpf
import pandas as pd
import Dukascopy_data_analysis as dda

eur_usd = dda.eur_usd

print(eur_usd.head())

eur_usd.rename(columns={'Gmt time': 'Date'}, inplace= True)

print(eur_usd.head())

eur_usd [['Date', 'Time']] = eur_usd.Date.str.split(expand=True)

print(eur_usd.head())

eur_usd = eur_usd[['Date', 'Time', 'Open', 'High', 'Low', 'Close', 'Volume']]

print(eur_usd.head())

eur_usd.Date = pd.to_datetime(eur_usd.Date)

print(eur_usd.info())
    
    