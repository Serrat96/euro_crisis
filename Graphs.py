import plotly.graph_objects as go
from plotly.offline import plot
import pandas as pd
#import src.currencies_data.eur_list_1H as eur1h
import src.currencies_data.eur_list_4H as eur4h
import src.currencies_data.eur_list_1D as eur1d
#import src.currencies_data.eur_list_1W as eur1w
import src.currencies_data.eur_list_1M as eur1m

#currencies_list_1h = eur1h.currencies_list_1h

currencies_list_4h = eur4h.currencies_list_4h

currencies_list_1d = eur1d.currencies_list_1d

#currencies_list_1w = eur1w.currencies_list_1w

currencies_list_1m = eur1m.currencies_list_1m

currencies_list = ['eur_aud', 'eur_cad', 'eur_chf', 'eur_czk', 'eur_dkk', 'eur_gbp', 'eur_hkd',\
                   'eur_huf', 'eur_jpy', 'eur_nok', 'eur_nzd', 'eur_pln', 'eur_rub', 'eur_sek',\
                   'eur_sgd', 'eur_try', 'eur_usd']
    
currencies_list = [i.upper() for i in currencies_list]

currencies_list = [j.replace('_', '/') for j in currencies_list]

print(currencies_list)

def candlestick_print(x):
    
    num = 0
    
    for i in x:
    
        df = pd.DataFrame(i)
        
        
    
        fig = go.Figure(data=[go.Candlestick(x=df['Gmt time'],#Preguntar si se puede poner fecha aqui o hay que procesar antes
                                             open=df['Open'],
                                             high=df['High'],
                                             low=df['Low'],
                                             close=df['Close'])])
        
        
        fig.update_layout(
            title=currencies_list[num],
            yaxis_title='Price')
    
        num += 1
        
        plot(fig)
        
        break
        
    print('Se han hecho', num, 'gráficas de', len(x), 'posibles')

candlestick_print(currencies_list_1d)
