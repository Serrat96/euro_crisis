import pandas as pd

eur_aud_daily = pd.read_csv("https://raw.githubusercontent.com/Serrat96/DukascopyData/master/DUKASCOPY_EUR_1H_BID/EURAUD_Candlestick_1_h_BID_07.10.2005-20.02.2021.csv")

eur_cad_daily = pd.read_csv("https://raw.githubusercontent.com/Serrat96/DukascopyData/master/DUKASCOPY_EUR_1H_BID/EURCAD_Candlestick_1_h_BID_25.10.2004-20.02.2021.csv")
      
eur_chf_daily = pd.read_csv("https://raw.githubusercontent.com/Serrat96/DukascopyData/master/DUKASCOPY_EUR_1H_BID/EURCHF_Candlestick_1_h_BID_03.08.2003-20.02.2021.csv")
    
eur_czk_daily = pd.read_csv("https://raw.githubusercontent.com/Serrat96/DukascopyData/master/DUKASCOPY_EUR_1H_BID/EURCZK_Candlestick_1_h_BID_02.01.2017-20.02.2021.csv")

eur_dkk_daily = pd.read_csv("https://raw.githubusercontent.com/Serrat96/DukascopyData/master/DUKASCOPY_EUR_1H_BID/EURDKK_Candlestick_1_h_BID_25.10.2004-20.02.2021.csv")
    
eur_gbp_daily = pd.read_csv("https://raw.githubusercontent.com/Serrat96/DukascopyData/master/DUKASCOPY_EUR_1H_BID/EURGBP_Candlestick_1_h_BID_03.08.2003-20.02.2021.csv")
    
eur_hkd_daily = pd.read_csv("https://raw.githubusercontent.com/Serrat96/DukascopyData/master/DUKASCOPY_EUR_1H_BID/EURHKD_Candlestick_1_h_BID_13.03.2007-20.02.2021.csv")
    
eur_huf_daily = pd.read_csv("https://raw.githubusercontent.com/Serrat96/DukascopyData/master/DUKASCOPY_EUR_1H_BID/EURHUF_Candlestick_1_h_BID_14.03.2007-20.02.2021.csv")

eur_jpy_daily = pd.read_csv("https://raw.githubusercontent.com/Serrat96/DukascopyData/master/DUKASCOPY_EUR_1H_BID/EURJPY_Candlestick_1_h_BID_03.08.2003-20.02.2021.csv")

eur_nok_daily = pd.read_csv("https://raw.githubusercontent.com/Serrat96/DukascopyData/master/DUKASCOPY_EUR_1H_BID/EURNOK_Candlestick_1_h_BID_25.10.2004-20.02.2021.csv")

eur_nzd_daily = pd.read_csv("https://raw.githubusercontent.com/Serrat96/DukascopyData/master/DUKASCOPY_EUR_1H_BID/EURNZD_Candlestick_1_h_BID_02.01.2006-20.02.2021.csv")

eur_pln_daily = pd.read_csv("https://raw.githubusercontent.com/Serrat96/DukascopyData/master/DUKASCOPY_EUR_1H_BID/EURPLN_Candlestick_1_h_BID_14.03.2007-20.02.2021.csv")

eur_rub_daily = pd.read_csv("https://raw.githubusercontent.com/Serrat96/DukascopyData/master/DUKASCOPY_EUR_1H_BID/EURRUB_Candlestick_1_h_BID_13.03.2007-20.02.2021.csv")

eur_sek_daily = pd.read_csv("https://raw.githubusercontent.com/Serrat96/DukascopyData/master/DUKASCOPY_EUR_1H_BID/EURSEK_Candlestick_1_h_BID_27.10.2004-20.02.2021.csv")

eur_sgd_daily = pd.read_csv("https://raw.githubusercontent.com/Serrat96/DukascopyData/master/DUKASCOPY_EUR_1H_BID/EURSGD_Candlestick_1_h_BID_13.03.2007-20.02.2021.csv")

eur_try_daily = pd.read_csv("https://raw.githubusercontent.com/Serrat96/DukascopyData/master/DUKASCOPY_EUR_1H_BID/EURTRY_Candlestick_1_h_BID_13.03.2007-20.02.2021.csv")

eur_usd_daily = pd.read_csv("https://raw.githubusercontent.com/Serrat96/DukascopyData/master/DUKASCOPY_EUR_1H_BID/EURUSD_Candlestick_1_h_BID_04.05.2003-20.02.2021.csv")

currencies_list_daily = [eur_aud_daily, eur_cad_daily, eur_chf_daily, eur_czk_daily, eur_dkk_daily, eur_gbp_daily, eur_hkd_daily,\
                   eur_huf_daily, eur_jpy_daily, eur_nok_daily, eur_nzd_daily, eur_pln_daily, eur_rub_daily, eur_sek_daily,\
                   eur_sgd_daily, eur_try_daily, eur_usd_daily]