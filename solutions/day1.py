import pandas as pd

root_dir = '/Users/jeremynadal/Documents/adventofcode/adventofcode2020/'
file_path = root_dir + 'inputs/input_1.txt'

data = pd.read_csv(file_path,sep='\n',header=None)
data.columns = ['raw']

###### Seconde part ###### 

for i in range(data.shape[0]):
    for j in range(i, data.shape[0]):
        for k in range(j, data.shape[0]):
            trois = data['raw'][k]
            oui = data['raw'][i]
            non = data['raw'][j]
            if oui + non + trois == 2020 : 
                print(oui,non,trois,oui*non*trois)

print(data.head(),data.columns)
