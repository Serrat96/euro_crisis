import pandas as pd
from datetime import datetime
#import src.currencies_data.eur_list_1H as eur1h
#import src.currencies_data.eur_list_4H as eur4h
import src.currencies_data.eur_list_1D as eur1d
#import src.currencies_data.eur_list_1W as eur1w
#import src.currencies_data.eur_list_1M as eur1m

#currencies_list_1h = eur1h.currencies_list_1h

#currencies_list_4h = eur4h.currencies_list_4h

currencies_list_1d = eur1d.currencies_list_1d

#currencies_list_1w = eur1w.currencies_list_1w

#currencies_list_1m = eur1m.currencies_list_1m

def filter_date(time_frame, from_date, to_date):

    num = 0
        
    currencies_list = ['eur_aud', 'eur_cad', 'eur_chf', 'eur_czk', 'eur_dkk', 'eur_gbp', 'eur_hkd',\
                   'eur_huf', 'eur_jpy', 'eur_nok', 'eur_nzd', 'eur_pln', 'eur_rub', 'eur_sek',\
                   'eur_sgd', 'eur_try', 'eur_usd']
    
    currencies_list = [i.upper() for i in currencies_list]

    currencies_list = [j.replace('_', '/') for j in currencies_list]
    
    filtered_by_data = []

    for df in time_frame:
    
        print('Para el par de monedas', currencies_list[num],'la cabecera es:')
        
        df.set_index('Gmt time')
        
        df['Gmt time'] = pd.to_datetime(df['Gmt time'])
        
        mask = (df['Gmt time'] >= datetime.strptime(from_date, '%Y-%m-%d')) &\
                (df['Gmt time'] <= datetime.strptime(to_date, '%Y-%m-%d'))
        
        df = df.loc[mask]
        
        print(df.head())
        
        print('\n')
        
        print('Para el par de monedas', currencies_list[num],'la cola es:')
        
        print(df.tail())
        
        print('\n')
        
        num += 1
        
        filtered_by_data.append(df)
        
    return filtered_by_data
    
crisis_2008 = filter_date(currencies_list_1d, '2007-01-01', '2009-01-01')

crisis_2012 = filter_data(currencies_list_1h, )