import plotly.graph_objects as go
import pandas as pd
from datetime import *
from Constants import *


def filter_date(time_frame, from_date, to_date):

    filtered_by_data = []

    num = 0

    for df in time_frame:

        df.set_index('Gmt time')

        df['Gmt time'] = pd.to_datetime(df['Gmt time'], format='%d.%m.%Y %H:%M:%S.%f')

        mask = (df['Gmt time'] >= datetime.strptime(from_date, '%Y-%m-%d')) & \
               (df['Gmt time'] <= datetime.strptime(to_date, '%Y-%m-%d'))

        df = df.loc[mask]

        print('\n')

        print('\n')

        num += 1

        filtered_by_data.append(df)

    return filtered_by_data


def candlestick_print(x):

    num = 0

    for df in x:
        fig = go.Figure(
            data=[go.Candlestick(x=df['Gmt time'],
                                 open=df['Open'],
                                 high=df['High'],
                                 low=df['Low'],
                                 close=df['Close'])])

        fig.update_layout(
            title=currencies_list[num],
            yaxis_title='Price',
            yaxis={'title': 'y-axis', 'scaleratio':2})

        fig.update_layout(yaxis_range=[7.4, 7.6])
        num += 1

        fig.show()
        if num == 5:
            break
    print('Se han hecho', num, 'gráficas de', len(x), 'posibles')

