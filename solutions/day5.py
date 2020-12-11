import pandas as pd
import numpy as np
import os
import re


def row_to_binary(raw_row):
    bin_row = re.sub('F','0',raw_row)
    bin_row = re.sub('B','1',bin_row)
    
    return bin_row

def col_to_binary(raw_col):
    bin_col = re.sub('R','1',raw_col)
    bin_col = re.sub('L','0',bin_col)
    return bin_col

def bin_to_num(binary):
    summ = 0
    binary = binary[::-1]
    for i in range(len(binary)) : 
        summ += int(binary[i])*2**i
    return summ

def convert_spec(spec):
    raw_row = spec[:7]
    raw_col = spec[7:]
    
    bin_row = row_to_binary(raw_row)
    bin_col = col_to_binary(raw_col)
    
    row = bin_to_num(bin_row)
    col = bin_to_num(bin_col)
    #print('raw:',raw_row,raw_col)
    #print('bin:',bin_row,bin_col)
    #print('num:',row,col)
    return row,col
    


root_dir = '/Users/jeremynadal/Documents/adventofcode/adventofcode2020/'
file_path = root_dir + 'inputs/input_5.txt'

if os.path.exists(file_path):
    data = pd.read_csv(file_path,sep = '\n', header = None)

data.columns = ['spec']

cols = []
rows = []
for raw in data['spec']:
    conv = convert_spec(raw)
    rows.append(conv[0])
    cols.append(conv[1])
data['row'] = rows
data['col'] = cols
data['seatID'] = 8*data['row']+data['col']


print('On the list, the max seat ID is',np.max(data['seatID']))

sorted_ID = np.sort(data['seatID'])
for ind in range(1,len(sorted_ID)-1):
    if not(sorted_ID[ind]-1 == sorted_ID[ind-1]):
        print('The only seat left is ',sorted_ID[ind]-1)