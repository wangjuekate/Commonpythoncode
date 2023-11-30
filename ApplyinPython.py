#collect the firms' rating on different capabilities
import numpy as np
from datetime import date
from datetime import datetime
import math
from datetime import timedelta
from dateutil.relativedelta import relativedelta, MO
from pandas import DataFrame
import pandas as pd
import os


#From Deal to Startup with AI patents, with linkedin
import pandas as pd
import numpy as np
import time
from string_grouper import match_strings
import os
from json import loads
import pandas as pd
from fuzzywuzzy import fuzz
import numpy as np
from datetime import date
import math
from datetime import timedelta
from dateutil.relativedelta import relativedelta, MO
import json
import concurrent.futures
import numpy
import sys
numpy.set_printoptions(threshold=sys.maxsize)
pd.options.display.max_rows = 1000
#system category
publicfirmpatents3= pd.read_stata('/Users/jjw6286/Library/CloudStorage/Dropbox/AI_Yong/Empirics/Variables/Patents/Startuppatent/Publicfirmpatentwithtech.dta')
startuppatents3 = pd.read_stata('/Users/jjw6286/Library/CloudStorage/Dropbox/AI_Yong/Empirics/Variables/Patents/Startuppatent/Startuppatentwithtech1.dta')
#add startup ai patent
AIpatent = pd.read_stata('/Users/jjw6286/Library/CloudStorage/Dropbox/WangjuekateDropbox/AI-basedEnterprises/Variables/AIinnovation/ai_model_predictions.dta')
print(AIpatent.iloc[1])
AIpatent_link = pd.read_csv('/Users/jjw6286/Library/CloudStorage/Dropbox/AI_Yong/Empirics/Variables/PatentApplication/g_application.tsv', sep="\t")
print(AIpatent_link.iloc[1])


AllpatentswithAI = AIpatent_link.merge(AIpatent, how = 'left', left_on = 'application_id', right_on ='appl_id' )
AllpatentswithAI = AllpatentswithAI.dropna()
AllpatentswithAI = AllpatentswithAI.fillna(0)
AllpatentswithAI['algorithm'] = AllpatentswithAI['ai_score_ml'] + AllpatentswithAI['ai_score_nlp']+AllpatentswithAI['ai_score_speech']+ AllpatentswithAI['ai_score_vision']

print(AllpatentswithAI['algorithm'].value_counts())

AllpatentswithAI['compute'] = AllpatentswithAI['ai_score_evo']+  AllpatentswithAI['ai_score_kr']+ AllpatentswithAI['ai_score_planning']+ AllpatentswithAI['ai_score_hardware']

AllpatentswithAI['data'] = AllpatentswithAI['ai_score_nlp']+AllpatentswithAI['ai_score_speech']+ AllpatentswithAI['ai_score_vision']

print(AllpatentswithAI['compute'].value_counts())
print(startuppatents3.iloc[1])
print(publicfirmpatents3.iloc[1])

AllpatentswithAI['patent_id'] = AllpatentswithAI['patent_id'].astype(str)


print(AllpatentswithAI['patent_id'])

AllpatentswithAI = AllpatentswithAI[['data','compute','algorithm', 'patent_id','application_id']]
AllpatentswithAI.to_stata('/Users/jjw6286/Library/CloudStorage/Dropbox/AI_Yong/Empirics/Variables/Patents/AIpatentcategory/AIpatent_connectpatentid.dta')

#assignee of the AI patents

print(publicfirmpatents3.iloc[1])



#calculate system complement, same industry but distant AI components
publicfirmpatents3 = publicfirmpatents3.merge(AllpatentswithAI, how ='left', left_on ='patent_id' , right_on ='patent_id' )
startuppatents3 = startuppatents3.merge(AllpatentswithAI, how ='left', left_on ='patent_id_x' , right_on ='patent_id' )
publicfirmpatents3= publicfirmpatents3.fillna(0)
startuppatents3= startuppatents3.fillna(0)
test = publicfirmpatents3['algorithm']+publicfirmpatents3['compute']+ publicfirmpatents3['data']
test =startuppatents3['algorithm']+startuppatents3['compute']+ startuppatents3['data']
print(test.value_counts())

#industry
industry = pd.read_csv('/Users/jjw6286/Library/CloudStorage/Dropbox/AI_Yong/Empirics/Variables/Publicfirmindustrycategory/publicfirmindustrycategory.csv', sep=',')
'gind','gvkey'
startupindustry = pd.read_json('/Users/jjw6286/Library/CloudStorage/Dropbox/AI_Yong/Empirics/Variables/AIventures/RawData/LinkedinAIfirms.json')
startupindustry = startupindustry['Industry'].drop_duplicates()
startupindustry.to_csv('/Users/jjw6286/Library/CloudStorage/Dropbox/AI_Yong/Empirics/Variables/Publicfirmindustrycategory/startupindustry.csv', sep =',', index= False)
startupindustry_add  = pd.read_table('/Users/jjw6286/Library/CloudStorage/Dropbox/AI_Yong/Empirics/Variables/Publicfirmindustrycategory/startupindustry.csv', sep =',')

startupindustry = startupindustry.merge(startupindustry_add, how='left', left_on = 'Industry', right_on ='Industry')
print(startupindustry.iloc[1])
startupindustry = startupindustry[['DocId','gindustry']]

startuppatents3 = startuppatents3.merge(startupindustry, how='left', left_on = 'DocId',right_on = 'DocId')
print(startuppatents3.iloc[1])

#public firm industry
industry = industry[['gvkey','gind']]
industry = industry.drop_duplicates()

publicfirmpatents3 = publicfirmpatents3.merge(industry, how='left', left_on = 'gvkey', right_on ='gvkey')

publicfirmpatents3['application_id'] = publicfirmpatents3['application_id'].astype(str)
publicfirmpatents3.to_stata('/Users/jjw6286/Library/CloudStorage/Dropbox/AI_Yong/Empirics/Variables/Patents/Startuppatent/Publicfirmpatentwithtech2.dta')

startuppatents3= startuppatents3.drop(['patent_id_x'], axis=1)
print(startuppatents3.iloc[1])
startuppatents3.to_stata('/Users/jjw6286/Library/CloudStorage/Dropbox/AI_Yong/Empirics/Variables/Patents/Startuppatent/Startuppatentwithtech2.dta')

#calculate the ecosystem complementary 
publicfirmpatents3 = publicfirmpatents3[['gvkey','algorithm','compute','data','gind','year']]
startuppatents3 = startuppatents3[['DocId','algorithm','compute','data','gindustry','year']]

publicfirmpatents3['gind_new'] = publicfirmpatents3['gind'].astype(str).str[:1]
startuppatents3['gindustry_new'] = startuppatents3['gindustry'].astype(str).str[:1]

#unify the industry

print(publicfirmpatents3['gind_new'].value_counts())
print(publicfirmpatents3['data'].value_counts())
startuppatents3= startuppatents3.fillna(0)
print(startuppatents3['gindustry_new'].value_counts())
publicfirmpatents3= publicfirmpatents3.fillna(0)
print(startuppatents3['data'].value_counts())

treatmentpanel= pd.read_stata('/Users/jjw6286/Library/CloudStorage/Dropbox/AI_Yong/Empirics/Datasets/panel2007_2017_treatment.dta')

treatmentpanel1= pd.read_stata('/Users/jjw6286/Library/CloudStorage/Dropbox/AI_Yong/Empirics/Datasets/panel2007_2017_addinvestment.dta')

print(treatmentpanel.iloc[1])


test = startuppatents3[startuppatents3['DocId'].isin(treatmentpanel['DocId'])] 
test['test'] =test['algorithm']+test['compute']+ test['data']
test= test[test['test']>0]
print(len(test['DocId'].drop_duplicates()))
print(test1.value_counts())

test = publicfirmpatents3[publicfirmpatents3['gvkey'].isin(treatmentpanel1['gvkey'])] 
test1 =test['algorithm']+test['compute']+ test['data']
print(test1.value_counts())

publicfirmpatents3 =publicfirmpatents3[ publicfirmpatents3['year']!='']

def techcomplement(input, startuppatents3, publicfirmpatents3):

#problem cannot find the matched class for startup and public firms
    startupinvention = startuppatents3[(startuppatents3['DocId'].astype(str)==input['DocId'])&(startuppatents3['year'].astype(int)<=input['year'])]
    print(startupinvention.values)

    publifirminvention = publicfirmpatents3[(publicfirmpatents3['gvkey']==input['gvkey'])&(publicfirmpatents3['year'].astype(int)<=input['year'])]
    print(publifirminvention.values)

    if((len(startupinvention.index)!=0) & (len(publifirminvention.index)!=0)):
        check = startupinvention.merge(publifirminvention, left_on ='gindustry', right_on ='gind')
        industrycompliment = len(check.index)
        matrix1 = numpy.array(startupinvention.iloc[:,1:4])
        matrix2 = numpy.array(publifirminvention.iloc[:,1:4])
        output = 0
        for i in range(len(matrix1)):
            for j in range(len(matrix2)):
                techcomplement = numpy.linalg.norm(matrix1[i]-matrix2[j])
                techcomplement =  np.nan_to_num(techcomplement, nan =0)
                output  = output +techcomplement
        techcomplement = output
    else:
        techcomplement=0
        industrycompliment=0
    return(industrycompliment,techcomplement)

addsystemcomplement = treatmentpanel.apply(techcomplement, axis=1,args=(startuppatents3, publicfirmpatents3))

output1 = list()
output2= list()
for i in range(len(addsystemcomplement)):
    a, b = addsystemcomplement[i]
    print(a,b)
    output1.append(a)
    output2.append(b)


treatmentpanel['industrycomplement'] =output1
treatmentpanel['systemcomplement2'] =output2
print(treatmentpanel['systemcomplement2'].value_counts())

print(treatmentpanel.iloc[1])
treatmentpanel = treatmentpanel.drop(['level_0'], axis=1)
treatmentpanel.to_stata('/Users/jjw6286/Library/CloudStorage/Dropbox/AI_Yong/Empirics/Datasets/panel2007_2017_treatment2.dta')

treatmentpanel = pd.read_stata('/Users/jjw6286/Library/CloudStorage/Dropbox/AI_Yong/Empirics/Datasets/panel2007_2017_treatment1.dta')




