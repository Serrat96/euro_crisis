currencies_list = ['eur_aud', 'eur_cad', 'eur_chf', 'eur_czk', 'eur_dkk', 'eur_gbp', 'eur_hkd', \
                   'eur_huf', 'eur_jpy', 'eur_nok', 'eur_nzd', 'eur_pln', 'eur_rub', 'eur_sek', \
                   'eur_sgd', 'eur_try', 'eur_usd']

currencies_list = [i.upper() for i in currencies_list]

currencies_list = [j.replace('_', '/') for j in currencies_list]

