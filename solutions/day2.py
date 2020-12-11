import pandas as pd

root_dir = '/Users/jeremynadal/Documents/adventofcode/adventofcode2020/'
file_path = root_dir + 'inputs/input_2.txt'

data = pd.read_csv(file_path,sep = '\n', header = None)
data.columns = ['raw']


check = []

for ind in range(data.shape[0]):
    min_letter = int(data['raw'][ind].split(' ')[0].split('-')[0])
    max_letter = int(data['raw'][ind].split(' ')[0].split('-')[1])
    letter     = data['raw'][ind].split(' ')[1].split(':')[0]
    passcode   = data['raw'][ind].split(' ')[2]

    check.append( (passcode.count(letter)<=max_letter) and  (passcode.count(letter)>=min_letter))
    
data['check'] = check

print('Total of valid passcodes for part 1 :',data['check'].sum())

check = []
for ind in range(data.shape[0]):
    first_letter = int(data['raw'][ind].split(' ')[0].split('-')[0])
    second_letter = int(data['raw'][ind].split(' ')[0].split('-')[1])
    letter     = data['raw'][ind].split(' ')[1].split(':')[0]
    passcode   = data['raw'][ind].split(' ')[2]

    check.append( (passcode[first_letter-1]==letter or passcode[second_letter-1]==letter ) 
                 and not (passcode[first_letter-1]==letter and passcode[second_letter-1]==letter ) )
data['check'] = check

print('Total of valid passcodes for part 2 :',data['check'].sum())

