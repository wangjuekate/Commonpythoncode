
from collections import Counter
def flatten_extend(matrix):
    flat_list = []
    for row in matrix:
            flat_list.extend(row)
    return flat_list

def issuecalculate(group):
    issues = group['issues'].str.split(pat =';', expand=True)
    issuecounts = flatten_extend(issues.values)
    issuecounts= [x for x in issuecounts if x is not None]
    issuevalue =  Counter(issuecounts)
    df3 = pd.DataFrame.from_dict(issuevalue, orient='index').reset_index()
    return df3


results = protestsclean.groupby(['statefips', 'countyfips','year']).apply(issuecalculate)

test = results.index.to_frame(index=False)
results = pd.DataFrame(results).reset_index(drop=True)
test['issues'] = results.iloc[:,0]
test['issuesnum'] = results.iloc[:,1]

