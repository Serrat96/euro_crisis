import mplfinance as mpf
import pandas as pd
import Dukascopy_data_analysis as dda

currencies_string = ['eur_aud', 'eur_cad', 'eur_chf', 'eur_czk', 'eur_dkk', 'eur_gbp', 'eur_hkd',\
                   'eur_huf', 'eur_jpy', 'eur_nok', 'eur_nzd', 'eur_pln', 'eur_rub', 'eur_sek',\
                   'eur_sgd', 'eur_try', 'eur_usd']
    
for i in range(len(currencies_string)):
    
    currencies_string[i] = currencies_string[i].upper()
    
    currencies_string[i] = currencies_string[i].replace('_', '/')

print(currencies_string)

num = 0



for dda.i in dda.currencies_list:
    
    i = dda.i

    i = i.set_index('Gmt time')

    i.index = pd.to_datetime(i.index)

    i = i.sort_index()
    
    try:
        
        mpf.plot(i['2007-09-28':'2007-10-20'],
                 type = 'candlestick',
                 volume = True,
                 title = currencies_string[num],
                 style = 'nightclouds')
        
        num += 1
        
    except:
        
        print("No hay datos para esta fecha para la moneda", currencies_string[num])
        
        num +=1