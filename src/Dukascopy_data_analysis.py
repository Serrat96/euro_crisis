import pandas as pd

eur_aud = pd.read_csv("..\DUKASCOPY_EUR_4H_BID\EURAUD_Candlestick_4_h_BID_07.10.2005-20.02.2021.csv")

eur_cad = pd.read_csv("..\DUKASCOPY_EUR_4H_BID\EURCAD_Candlestick_4_h_BID_25.10.2004-20.02.2021.csv")
      
eur_chf = pd.read_csv("..\DUKASCOPY_EUR_4H_BID\EURCHF_Candlestick_1_h_BID_03.08.2003-20.02.2021.csv")
    
eur_czk = pd.read_csv("..\DUKASCOPY_EUR_4H_BID\EURCZK_Candlestick_4_h_BID_02.01.2017-20.02.2021.csv")

eur_dkk = pd.read_csv("..\DUKASCOPY_EUR_4H_BID\EURDKK_Candlestick_4_h_BID_25.10.2004-20.02.2021.csv")
    
eur_gbp = pd.read_csv("..\DUKASCOPY_EUR_4H_BID\EURGBP_Candlestick_4_h_BID_03.08.2003-20.02.2021.csv")
    
eur_hkd = pd.read_csv("..\DUKASCOPY_EUR_4H_BID\EURHKD_Candlestick_4_h_BID_13.03.2007-20.02.2021.csv")
    
eur_huf = pd.read_csv("..\DUKASCOPY_EUR_4H_BID\EURHUF_Candlestick_4_h_BID_14.03.2007-20.02.2021.csv")

eur_jpy = pd.read_csv("..\DUKASCOPY_EUR_4H_BID\EURJPY_Candlestick_4_h_BID_03.08.2003-20.02.2021.csv")

eur_nok = pd.read_csv("..\DUKASCOPY_EUR_4H_BID\EURNOK_Candlestick_4_h_BID_25.10.2004-20.02.2021.csv")

eur_nzd = pd.read_csv("..\DUKASCOPY_EUR_4H_BID\EURNZD_Candlestick_4_h_BID_02.01.2006-20.02.2021.csv")

eur_pln = pd.read_csv("..\DUKASCOPY_EUR_4H_BID\EURPLN_Candlestick_4_h_BID_14.03.2007-20.02.2021.csv")

eur_rub = pd.read_csv("..\DUKASCOPY_EUR_4H_BID\EURRUB_Candlestick_4_h_BID_13.03.2007-20.02.2021.csv")

eur_sek = pd.read_csv("..\DUKASCOPY_EUR_4H_BID\EURSEK_Candlestick_4_h_BID_27.10.2004-20.02.2021.csv")

eur_sgd = pd.read_csv("..\DUKASCOPY_EUR_4H_BID\EURSGD_Candlestick_4_h_BID_13.03.2007-20.02.2021.csv")

eur_try= pd.read_csv("..\DUKASCOPY_EUR_4H_BID\EURTRY_Candlestick_4_h_BID_13.03.2007-20.02.2021.csv")

#eur_usd = pd.read_csv("..\DUKASCOPY_EUR_4H_BID\EURUSD_Candlestick_4_h_BID_04.05.2003-20.02.2021.csv")

eur_usd = pd.read_csv("..\DUKASCOPY_EUR_DAILY_BID\EURUSD_Candlestick_1_D_BID_04.05.2003-20.02.2021.csv")

currencies_list = [eur_aud, eur_cad, eur_chf, eur_czk, eur_dkk, eur_gbp, eur_hkd,\
                   eur_huf, eur_jpy, eur_nok, eur_nzd, eur_pln, eur_rub, eur_sek,\
                   eur_sgd, eur_try, eur_usd]