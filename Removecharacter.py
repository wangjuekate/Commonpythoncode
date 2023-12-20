int(''.join(filter(str.isdigit, '200 grams 5')))
privatefirminvestor3['vrdamtsume_test'] = privatefirminvestor3['vrdamtsume'].str.replace(',', '', regex=True)
privatefirminvestor3.loc[(privatefirminvestor3['vrdamtsume_test']==''),'vrdamtsume_test'] = '0'
privatefirminvestor3['vrdamtsume_test'] = privatefirminvestor3['vrdamtsume_test'].astype(float)

