
hacktivismannounce= pd.DataFrame()
directory = "/Users/jjw6286/Nextcloud/Activeproject/Hacktivism_Mark/RawData/LexisNexisHacktivism/Allhacktivismnews"
for root,dirs,files in os.walk(directory):
    for file in files:
       if file.endswith(".json"):
           pathnew = os.path.join(directory, file)
           print(pathnew)
           data=pd.read_json(pathnew)
           test = data[data['Body'].str.contains('protest')]
           output = test
           hacktivismannounce= pd.concat([hacktivismannounce,output], ignore_index=True)
hacktivismannounce = hacktivismannounce.drop_duplicates()
hacktivismannounce1 = hacktivismannounce[~hacktivismannounce['Body'].str.contains('government')]
hacktivismannounce1 = hacktivismannounce1[hacktivismannounce1['Body'].str.contains('company')]
print(hacktivismannounce1['Year'].value_counts())
print(hacktivismannounce1.iloc[1].values)
