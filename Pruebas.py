import pandas as pd
from datetime import datetime
#import src.currencies_data.eur_list_1H as eur1h
#import src.currencies_data.eur_list_4H as eur4h
#import src.currencies_data.eur_list_1D as eur1d
#import src.currencies_data.eur_list_1W as eur1w
import src.currencies_data.eur_list_1M as eur1m

#currencies_list_1h = eur1h.currencies_list_1h

#currencies_list_4h = eur4h.currencies_list_4h

#currencies_list_1d = eur1d.currencies_list_1d

#currencies_list_1w = eur1w.currencies_list_1w

currencies_list_1m = eur1m.currencies_list_1m

num = 0

for i in currencies_list_1m:
    
    currencies_list = ['eur_aud', 'eur_cad', 'eur_chf', 'eur_czk', 'eur_dkk', 'eur_gbp', 'eur_hkd',\
                   'eur_huf', 'eur_jpy', 'eur_nok', 'eur_nzd', 'eur_pln', 'eur_rub', 'eur_sek',\
                   'eur_sgd', 'eur_try', 'eur_usd']
    
    currencies_list = [i.upper() for i in currencies_list]

    currencies_list = [j.replace('_', '/') for j in currencies_list]

    print('Para el par de monedas', currencies_list[num],'la cabecera es:')
    
    i.set_index('Gmt time')
    
    i['Gmt time'] = pd.to_datetime(i['Gmt time'])
    
    mask = (i['Gmt time'] >= datetime.strptime('2007-01-01', '%Y-%m-%d')) &\
            (i['Gmt time'] <= datetime.strptime('2009-01-01', '%Y-%m-%d'))
    
    i = i.loc[mask]
    
    print(i.head())
    
    print('\n')
    
    print('Para el par de monedas', currencies_list[num],'la cola es:')
    
    print(i.tail())
    
    print('\n')
    
    num += 1