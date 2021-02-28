import pandas as pd
import Dukascopy_data_analysis as dda

currencies_list = dda.currencies_list
num = 0

currencies_string = ['eur_aud', 'eur_cad', 'eur_chf', 'eur_czk', 'eur_dkk', 'eur_gbp', 'eur_hkd',\
                   'eur_huf', 'eur_jpy', 'eur_nok', 'eur_nzd', 'eur_pln', 'eur_rub', 'eur_sek',\
                   'eur_sgd', 'eur_try', 'eur_usd']
    
for i in range(len(currencies_string)):
    
    currencies_string[i] = currencies_string[i].upper()
    
    currencies_string[i] = currencies_string[i].replace('_', '/')   
    
for dda.i in currencies_list:
    
    i = dda.i
    
    print('Para el par de monedas', currencies_string[num], 'los datos nulos son:')
    
    print(pd.isnull(i).sum())
    
    num += 1
    
    if pd.isnull(i['Date time'])