from itertools import groupby
s=input()
for i,j in groupby(s):
    #groupby returns occurend and list of occurence
    #coverting it to output format
    print('('+str(len(list(j)))+', '+str(i)+')',end=" ")
    
