import pandas as pd

"""eur_aud_daily = pd.read_csv(
    "https://raw.githubusercontent.com/Serrat96/DukascopyData/master/DUKASCOPY_EUR_1D_BID/EURAUD_Candlestick_1_D_BID_07.10.2005-20.02.2021.csv")

eur_gbp_daily = pd.read_csv(
    "https://raw.githubusercontent.com/Serrat96/DukascopyData/master/DUKASCOPY_EUR_1D_BID/EURGBP_Candlestick_1_D_BID_03.08.2003-20.02.2021.csv")

eur_jpy_daily = pd.read_csv(
    "https://raw.githubusercontent.com/Serrat96/DukascopyData/master/DUKASCOPY_EUR_1D_BID/EURJPY_Candlestick_1_D_BID_03.08.2003-20.02.2021.csv")

eur_usd_daily = pd.read_csv(
    "https://raw.githubusercontent.com/Serrat96/DukascopyData/master/DUKASCOPY_EUR_1D_BID/EURUSD_Candlestick_1_D_BID_04.05.2003-20.02.2021.csv")"""

eur_aud_daily = pd.read_csv(r"C:\Users\serra\REPOSITORIOS\DukascopyData\DUKASCOPY_EUR_1D_BID\EURAUD_Candlestick_1_D_BID_07.10.2005-20.02.2021.csv")

eur_gbp_daily = pd.read_csv(r"C:\Users\serra\REPOSITORIOS\DukascopyData\DUKASCOPY_EUR_1D_BID\EURGBP_Candlestick_1_D_BID_03.08.2003-20.02.2021.csv")

eur_jpy_daily = pd.read_csv(r"C:\Users\serra\REPOSITORIOS\DukascopyData\DUKASCOPY_EUR_1D_BID\EURJPY_Candlestick_1_D_BID_03.08.2003-20.02.2021.csv")

eur_usd_daily = pd.read_csv(r"C:\Users\serra\REPOSITORIOS\DukascopyData\DUKASCOPY_EUR_1D_BID\EURUSD_Candlestick_1_D_BID_04.05.2003-20.02.2021.csv")

currencies_list_1d = [eur_aud_daily, eur_gbp_daily, eur_jpy_daily, eur_usd_daily]
