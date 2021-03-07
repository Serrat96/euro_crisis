import pandas as pd

eur_aud_1h = pd.read_csv("https://raw.githubusercontent.com/Serrat96/DukascopyData/master/DUKASCOPY_EUR_1H_BID/EURAUD_Candlestick_1_h_BID_07.10.2005-20.02.2021.csv")

eur_cad_1h = pd.read_csv("https://raw.githubusercontent.com/Serrat96/DukascopyData/master/DUKASCOPY_EUR_1H_BID/EURCAD_Candlestick_1_h_BID_25.10.2004-20.02.2021.csv")
      
eur_chf_1h = pd.read_csv("https://raw.githubusercontent.com/Serrat96/DukascopyData/master/DUKASCOPY_EUR_1H_BID/EURCHF_Candlestick_1_h_BID_03.08.2003-20.02.2021.csv")

eur_dkk_1h = pd.read_csv("https://raw.githubusercontent.com/Serrat96/DukascopyData/master/DUKASCOPY_EUR_1H_BID/EURDKK_Candlestick_1_h_BID_25.10.2004-20.02.2021.csv")
    
eur_gbp_1h = pd.read_csv("https://raw.githubusercontent.com/Serrat96/DukascopyData/master/DUKASCOPY_EUR_1H_BID/EURGBP_Candlestick_1_h_BID_03.08.2003-20.02.2021.csv")
    
eur_hkd_1h = pd.read_csv("https://raw.githubusercontent.com/Serrat96/DukascopyData/master/DUKASCOPY_EUR_1H_BID/EURHKD_Candlestick_1_h_BID_13.03.2007-20.02.2021.csv")
    
eur_huf_1h = pd.read_csv("https://raw.githubusercontent.com/Serrat96/DukascopyData/master/DUKASCOPY_EUR_1H_BID/EURHUF_Candlestick_1_h_BID_14.03.2007-20.02.2021.csv")

eur_jpy_1h = pd.read_csv("https://raw.githubusercontent.com/Serrat96/DukascopyData/master/DUKASCOPY_EUR_1H_BID/EURJPY_Candlestick_1_h_BID_03.08.2003-20.02.2021.csv")

eur_nok_1h = pd.read_csv("https://raw.githubusercontent.com/Serrat96/DukascopyData/master/DUKASCOPY_EUR_1H_BID/EURNOK_Candlestick_1_h_BID_25.10.2004-20.02.2021.csv")

eur_nzd_1h = pd.read_csv("https://raw.githubusercontent.com/Serrat96/DukascopyData/master/DUKASCOPY_EUR_1H_BID/EURNZD_Candlestick_1_h_BID_02.01.2006-20.02.2021.csv")

eur_pln_1h = pd.read_csv("https://raw.githubusercontent.com/Serrat96/DukascopyData/master/DUKASCOPY_EUR_1H_BID/EURPLN_Candlestick_1_h_BID_14.03.2007-20.02.2021.csv")

eur_rub_1h = pd.read_csv("https://raw.githubusercontent.com/Serrat96/DukascopyData/master/DUKASCOPY_EUR_1H_BID/EURRUB_Candlestick_1_h_BID_13.03.2007-20.02.2021.csv")

eur_sek_1h = pd.read_csv("https://raw.githubusercontent.com/Serrat96/DukascopyData/master/DUKASCOPY_EUR_1H_BID/EURSEK_Candlestick_1_h_BID_27.10.2004-20.02.2021.csv")

eur_sgd_1h = pd.read_csv("https://raw.githubusercontent.com/Serrat96/DukascopyData/master/DUKASCOPY_EUR_1H_BID/EURSGD_Candlestick_1_h_BID_13.03.2007-20.02.2021.csv")

eur_try_1h = pd.read_csv("https://raw.githubusercontent.com/Serrat96/DukascopyData/master/DUKASCOPY_EUR_1H_BID/EURTRY_Candlestick_1_h_BID_13.03.2007-20.02.2021.csv")

eur_usd_1h = pd.read_csv("https://raw.githubusercontent.com/Serrat96/DukascopyData/master/DUKASCOPY_EUR_1H_BID/EURUSD_Candlestick_1_h_BID_04.05.2003-20.02.2021.csv")

currencies_list_1h = [eur_aud_1h, eur_cad_1h, eur_chf_1h, eur_dkk_1h, eur_gbp_1h, eur_hkd_1h,\
                   eur_huf_1h, eur_jpy_1h, eur_nok_1h, eur_nzd_1h, eur_pln_1h, eur_rub_1h, eur_sek_1h,\
                   eur_sgd_1h, eur_try_1h, eur_usd_1h]