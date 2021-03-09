import plotly.graph_objects as go
import pandas as pd
from datetime import *
from Constants import *
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np
import matplotlib

def dukascopy_filter_date(list_of_currencies, from_date, to_date):

    filtered_by_data = []

    num = 0

    for df in list_of_currencies:

        df.set_index('Gmt time')

        df['Gmt time'] = pd.to_datetime(df['Gmt time'], format='%d.%m.%Y %H:%M:%S.%f')

        mask = (df['Gmt time'] >= datetime.strptime(from_date, '%Y-%m-%d')) & \
               (df['Gmt time'] <= datetime.strptime(to_date, '%Y-%m-%d'))

        df = df.loc[mask]

        print('\n')

        print('\n')

        num += 1

        filtered_by_data.append(df)

    print('Se han filtrado', num, 'dataframes de', len(list_of_currencies), 'posibles')

    return filtered_by_data


def correlation_dataframe(filtered_dataframes, graph_title):

    column_selected_df_list = []

    i = 0

    for df in filtered_dataframes:

        df = df.rename(columns={'Open': currencies_list[i]})

        df = df.reset_index(drop=True)

        column_selected_df_list.append(df[currencies_list[i]])

        i += 1

    corr_df = pd.concat(column_selected_df_list, axis=1)

    df_small = corr_df.iloc[:, :]

    correlation_map = df_small.corr()

    ax = plt.axes()

    mask = np.triu(np.ones_like(correlation_map, dtype=bool))

    cmap = matplotlib.colors.LinearSegmentedColormap.from_list("", colors)

    sns.heatmap(correlation_map, vmin=-1, vmax=1, mask=mask, ax=ax, annot=True, linewidths = 1.5,
                cmap=cmap, annot_kws={'size': 30})

    plt.text(0, -0.5, graph_title, fontsize = 20, color='Black', fontstyle='normal')

    plt.show()


def candlestick_print_2_annotations(dataframe_list, annotation_date_1, annotation_date_2, annotation_text_1, annotation_text_2):

    num = 0

    for df in dataframe_list:
        fig = go.Figure(
            data=[go.Candlestick(x=df['Gmt time'],
                                 open=df['Open'],
                                 high=df['High'],
                                 low=df['Low'],
                                 close=df['Close'])])

        fig.update_layout(
            title=currencies_list[num],
            yaxis_title='Price',
            xaxis_rangeslider_visible=False,
            shapes=[dict(x0=annotation_date_1, x1=annotation_date_1, y0=0, y1=1, xref='x', yref='paper', line_width=2),
                    dict(x0=annotation_date_2, x1=annotation_date_2, y0=0, y1=1, xref='x', yref='paper', line_width=2),
                    dict(x0=annotation_date_2, x1=annotation_date_2, y0=0, y1=1, xref='x', yref='paper', line_width=2)],
            annotations=[dict(x=annotation_date_1, y=0.95, xref='x', yref='paper', showarrow=False, xanchor='right', text=annotation_text_1),
                         dict(x=annotation_date_2, y=0.95, xref='x', yref='paper', showarrow=False, xanchor='left', text=annotation_text_2)])

        if num == 4:

            fig.update_layout(yaxis_range=[7.4, 7.6])

        num += 1

        fig.show()

    print('Se han hecho', num, 'gráficas de', len(dataframe_list), 'posibles')


def candlestick_print_4_annotations(dataframe_list,
                                    annotation_date_1, annotation_date_2, annotation_date_3, annotation_date_4,
                                    annotation_text_1, annotation_text_2, annotation_text_3, annotation_text_4):

    num = 0

    for df in dataframe_list:
        fig = go.Figure(
            data=[go.Candlestick(x=df['Gmt time'],
                                 open=df['Open'],
                                 high=df['High'],
                                 low=df['Low'],
                                 close=df['Close'])])

        fig.update_layout(
            title=currencies_list[num],
            yaxis_title='Price',
            xaxis_rangeslider_visible=False,
            shapes=[dict(x0=annotation_date_1, x1=annotation_date_1, y0=0, y1=1, xref='x', yref='paper', line_width=2),
                    dict(x0=annotation_date_2, x1=annotation_date_2, y0=0, y1=1, xref='x', yref='paper', line_width=2),
                    dict(x0=annotation_date_3, x1=annotation_date_3, y0=0, y1=1, xref='x', yref='paper', line_width=2),
                    dict(x0=annotation_date_4, x1=annotation_date_4, y0=0, y1=1, xref='x', yref='paper', line_width=2)],
            annotations=[dict(x=annotation_date_1, y=0.95, xref='x', yref='paper', showarrow=False, xanchor='right',text=annotation_text_1),
                         dict(x=annotation_date_2, y=0.01, xref='x', yref='paper', showarrow=False, xanchor='left', text=annotation_text_2),
                         dict(x=annotation_date_3, y=0.95, xref='x', yref='paper', showarrow=False, xanchor='right',text=annotation_text_3),
                         dict(x=annotation_date_4, y=0.01, xref='x', yref='paper', showarrow=False, xanchor='left', text=annotation_text_4)])

        if num == 4:

            fig.update_layout(yaxis_range=[7.4, 7.6])

        num += 1

        fig.show()

    print('Se han hecho', num, 'gráficas de', len(dataframe_list), 'posibles')