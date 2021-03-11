from Functions import *
import src.currencies_data.eur_list_1D as eur1d

"""Partimos de distintos dataframes con período de un día los cuales tenemos que filtrar por fechas para poder graficar
el período más adecuado"""

#crisis_2008 = dukascopy_filter_date(eur1d.currencies_list_1d, '2007-01-01', '2009-12-01')

#european_debt_2012 = dukascopy_filter_date(eur1d.currencies_list_1d, '2009-10-01', '2013-01-01')

#corralito_2013 = dukascopy_filter_date(eur1d.currencies_list_1d, '2012-02-01', '2013-06-01')

crisis_covid = dukascopy_filter_date(eur1d.currencies_list_1d, '2019-11-20', '2020-10-30')

"""candlestick_print_2_annotations(crisis_2008,
                                '2007-08-01', '2009-06-01',
                                'Comienza la desconfianza', 'Termina la desconfianza')


candlestick_print_2_annotations(european_debt_2012,
                                 '2010-05-02', '2012-02-21',
                                 'Concesion 1er rescate Grecia', 'Concesion 2do rescate Grecia',)"""

"""candlestick_print_3_annotations(corralito_2013,
                                '2012-06-27', '2013-03-15', '2013-03-28',
                                'Concesión rescate Chipre', 'Inicio corralito Chipre', 'Fin corralito Chipre',)"""

candlestick_print_2_annotations(crisis_covid,
                                '2020-02-01', '2020-09-01',
                                'Inicio crisis COVID-19', 'Fin crisis COVID-19')

#correlation_dataframe(crisis_2008, "")

#correlation_dataframe(european_debt_2012, '')

#correlation_dataframe(corralito_2013, "")

#correlation_dataframe(crisis_covid, "")