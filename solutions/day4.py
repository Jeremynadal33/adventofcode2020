import pandas as pd
import numpy as np
import os
import re

root_dir = '/Users/jeremynadal/Documents/adventofcode/adventofcode2020/'
file_path = root_dir + 'inputs/input_4.txt'

if os.path.exists(file_path):
    file = open(file_path,'r')
    
raw = file.read()
raw = raw[:-1] # Last character being '\n' 

raw = raw.split('\n\n') 

raw = [re.sub('\n',' ',r) for r in raw ]

data = pd.DataFrame(columns=['byr','iyr','eyr', 'hgt', 'hcl', 'ecl', 'pid','cid'])

for passport in raw : 
    passport = passport.split(' ')
    dic = {}
    for info in passport : 
        dic[info.split(':')[0]] = info.split(':')[1]
    data = data.append(dic,ignore_index=True)
    

data.drop('cid', axis = 1, inplace = True)
data.dropna(axis=0,inplace=True)
print('There is a total of {} valid passport for part 1 '.format(data.shape[0]))


# Lets do some further cleaning for part 2 

data['byr'] = data['byr'].astype(int)
data['iyr'] = data['iyr'].astype(int)
data['eyr'] = data['eyr'].astype(int)

# Putting one filter per condition
data = data[ 1920 <= data['byr'] ]
data = data[ data['byr'] <= 2002 ]

data = data[ 2010 <= data['iyr'] ]
data = data[ data['iyr'] <= 2020 ]

data = data[ 2020 <= data['eyr'] ]
data = data[ data['eyr'] <= 2030 ]

# For the other characteristics, must do differently
valid_ecl = ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth']

# For the other characteristics, must do differently
valid_ecl = ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth']

for ind in data.index : 
    to_drop = False
    # Looking for invalid height
    if data['hgt'][ind][-2:]=='cm':
        if (150 <= int(data['hgt'][ind][:-2]) ) and ( int(data['hgt'][ind][:-2]) <= 193) :
            pass
        else : 
            to_drop = True
    elif data['hgt'][ind][-2:]=='in':
        if (59 <= int(data['hgt'][ind][:-2]) ) and ( int(data['hgt'][ind][:-2]) <= 76) :
            pass
        else : 
            to_drop = True
    else :
        to_drop = True
        
        
    # Looking for invalid hair color 
    if (data['hcl'][ind][0]=='#' and len(re.findall('[0-9A-Fa-f]',data['hcl'][ind] )) == 6) :
        pass
    else : 
        to_drop = True
        
    # Looking for invalid eye color 
    if data['ecl'][ind] in valid_ecl : 
        pass
    else : 
        to_drop = True
    
    # Looking for invalid pid 
    if len(re.findall('[0-9A-Fa-f]', data['pid'][ind] )) == 9 :
        pass
    else :
        to_drop = True
        
    if to_drop : data.drop(ind, axis = 0, inplace = True)
        
print('The number of valid passport after part 2 is', data.shape[0])