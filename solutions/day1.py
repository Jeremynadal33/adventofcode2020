import pandas as pd

data = pd.read_csv('input.txt',sep='\n',header=None)
data.columns = ['raw']

for i in range(data.shape[0]):
    for j in range(data.shape[0]):
        for k in range(data.shape[0]):
            trois = data['raw'][k]
            oui = data['raw'][i]
            non = data['raw'][j]
            if oui + non + trois == 2020 : 
                print(oui,non,trois,oui*non*trois)

print(data.head(),data.columns)
