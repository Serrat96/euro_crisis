import pandas as pd

#import src.currencies_data.eur_list_1H as eur1h

#import src.currencies_data.eur_list_4H as eur4h

#import src.currencies_data.eur_list_1D as eur1d

#import src.currencies_data.eur_list_1W as eur1w

import src.currencies_data.eur_list_1M as eur1m

tot = len(eur1m.currencies_list_monthly)
num = 0

currencies_list_monthly = eur1m.currencies_list_monthly


#Quiero convertir la lista de csv en una lista de dataframe
for i in currencies_list_monthly:
    
    currencies_list_monthly[i] = pd.DataFrame()
    
    currencies_list_monthly[i] = currencies_list_monthly[['Open']]
    
    print(currencies_list_monthly[i].head())