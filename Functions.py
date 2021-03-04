import plotly.graph_objects as go
from plotly.offline import plot
import pandas as pd


def candlestick_print(x):
    num = 0

    for df in x:
        fig = go.Figure(
            data=[go.Candlestick(x=df['Gmt time'],  # Preguntar si se puede poner fecha aqui o hay que procesar antes
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


candlestick_print(currencies_list_1d)
    
    

        
        