for index, row in p.iterrows():
    if i > len(p):
       break
    else:
       f = open(str(i)+'.txt', 'w')
       f.write(row[0])
       f.close()
       i+=1
