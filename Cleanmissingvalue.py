
universitylocation['inst_zip'] = universitylocation['inst_zip'].str.extract('(\d+)')
universitylocation= universitylocation.fillna('0')
universitylocation['inst_zip'] = universitylocation['inst_zip'].astype(int)
universitylocation = universitylocation.replace(r'^\s*$', np.nan, regex=True)

publicfirmpanellocation['vzip'] = publicfirmpanellocation['vzip'].str.extract('(\d+)')
publicfirmpanellocation = publicfirmpanellocation.replace(r'^\s*$', np.nan, regex=True)
publicfirmpanellocation = publicfirmpanellocation.fillna('0')
publicfirmpanellocation['zip'] = publicfirmpanellocation['zip'].astype(int)
publicfirmpanellocation['vzip'] = publicfirmpanellocation['vzip'].astype(int)
publicfirmpanellocation = publicfirmpanellocation.drop_duplicates()
