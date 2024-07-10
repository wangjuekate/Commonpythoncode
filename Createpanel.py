listofindustry = finalall['vsic'].drop_duplicates()
listyear = np.arange(1954,2023,1)
outputall = pd.DataFrame()
for industryvalue in listofindustry: 
    output = pd.DataFrame([industryvalue])
    for value in listyear:
        output['year'] =int(value)
        outputall = pd.concat([outputall,output],ignore_index=True)
outputall.columns = ['vsic','year']
outputall = outputall.merge(industryconcentration,how ='left', left_on = ['vsic','year'],right_on = ['ic','year'])
outputall = outputall.sort_values(by = ['vsic','year'])
outputall = outputall.fillna(method='backfill')
outputall.columns = ['vsic','year','sicHHI','sictop4sales','vsicmerge']
finalall = finalall.merge(outputall, how= 'left', left_on = ['vsic','year'], right_on = ['vsic','year'])
finalall = finalall.fillna(0)
finalall.to_stata('/Users/jjw6286/Library/CloudStorage/Dropbox/AI_Yong/Empirics/Datasets/NewPanel/PanelConstruction/Regressiondata8.dta', write_index=False)
