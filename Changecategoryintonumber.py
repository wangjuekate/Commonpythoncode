#startup ages
pairaddcontrol['startupage'] = pairaddcontrol['year']- pairaddcontrol['vfoundyr']

pairaddcontrol['stagenum'] = pairaddcontrol['vstage1']
pairaddcontrol['stagenum'].replace(['Startup/Seed', 'Early Stage','Expansion','Later Stage','Buyout/Acquisition','Other'],
                        [1, 2,3,4,5,6], inplace=True)

print(pairaddcontrol['stagenum'].value_counts())

pairaddcontrol =  pairaddcontrol.groupby(['uuid','year']).first().reset_index()
