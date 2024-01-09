applicationinfo[['first','second']]=applicationinfo['application_id'].str.split(pat ='/', expand = True)

df3 = protests['date'].str.split(pat ='-', expand=True)
df3.columns = ['STATUS_ID{}'.format(x+1) for x in df3.columns]

protests[['year','month','day'] ]=df3[['STATUS_ID1','STATUS_ID2', 'STATUS_ID3']]

