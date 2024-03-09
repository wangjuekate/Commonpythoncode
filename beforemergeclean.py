
tomerge = treatmentpanel[['DocId','gvkey','year','pairid']]
tomerge['gvkey']= tomerge['gvkey'].astype(int)
tomerge = tomerge.fillna(0)
publicfirmstrength['gvkey']=publicfirmstrength['gvkey'].astype(int)

tomerge['year']= tomerge['year'].astype(int)
publicfirmstrength= publicfirmstrength[publicfirmstrength['year']!='']
publicfirmstrength['year']=publicfirmstrength['year'].astype(int)


tomerge1 = tomerge.merge(publicfirmstrength, how = 'left',left_on =['gvkey','year'], right_on = ['gvkey','year'])
