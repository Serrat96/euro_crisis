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

for i in currencies_list_1m:
    
    i.set_index('Gmt time')
    
    i['Gmt time'] = pd.to_datetime(i['Gmt time'])
    
    
    
    mask = (i['Gmt time'] >= datetime.strptime('2007-01-01', '%Y-%m-%d')) &\
            (i['Gmt time'] <= datetime.strptime('2009-01-01', '%Y-%m-%d'))
    
    i = i.loc[mask]
    
    print(i.head())