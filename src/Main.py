from Functions import *
from Constants import *
import src.currencies_data.eur_list_1D as eur1d

"""Partimos de distintos dataframes con período de un día los cuales tenemos que filtrar por fechas para poder graficar
el período más adecuado"""

crisis_2008 = filter_date(eur1d.currencies_list_1d, '2007-01-01', '2009-01-01')

corralito_2013 = filter_date(eur1d.currencies_list_1d, '2012-06-01', '2013-06-01')
num = 0

for df in crisis_2008:

    print('Para el par de monedas', currencies_list[num], 'la cabecera es:')

    print(df.head())

    print('Para el par de monedas', currencies_list[num], 'la cola es:')

    print(df.tail(),'\n')

    num += 1

print('hola')
candlestick_print(crisis_2008)
