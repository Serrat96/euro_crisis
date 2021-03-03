import plotly.graph_objects as go
from plotly.offline import plot
import pandas as pd

def candlestick_print(x):
    
    currencies_list = ['eur_aud', 'eur_cad', 'eur_chf', 'eur_czk', 'eur_dkk', 'eur_gbp', 'eur_hkd',\
                   'eur_huf', 'eur_jpy', 'eur_nok', 'eur_nzd', 'eur_pln', 'eur_rub', 'eur_sek',\
                   'eur_sgd', 'eur_try', 'eur_usd']
    
    currencies_list = [i.upper() for i in currencies_list]

    currencies_list = [j.replace('_', '/') for j in currencies_list]
    
    num = 0
    
    for i in x:
    
        df = pd.DataFrame(i)
        
        
    
        fig = go.Figure(data=[go.Candlestick(x=df['Gmt time',#Preguntar si se puede poner fecha aqui o hay que procesar antes
                                             open=df['Open'],
                                             high=df['High'],
                                             low=df['Low'],
                                             close=df['Close'])])
        
        
        fig.update_layout(
            title=currencies_list[num],
            yaxis_title='Price')
    
        num += 1
        
        plot(fig)
        
    print('Se han hecho', num, 'gráficas de', len(x), 'posibles')
    
    
def data_filtering(x):
    
    for i in x:
        
        df = pd.DataFrame(i)
        
        df['Gmt date'] =  pd.to_datetime(df['Gmt date'], format='%d%b%Y')
        
        