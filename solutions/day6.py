import pandas as pd
import numpy as np
import os
import re


root_dir = '/Users/jeremynadal/Documents/adventofcode/adventofcode2020/'
file_path = root_dir + 'inputs/input_6.txt'

if os.path.exists(file_path):
    file = open(file_path,'r')
    
raw = file.read()
raw = raw[:-1]

groups = raw.split('\n\n')

summ = 0
for group in groups : 
    group = re.sub('\n','',group)
    group = [g for g in group]
    group = np.unique(group)
    
    summ += len(group)
print('For part 1, the sum is :',summ)

summ = 0
for group in groups : 
    nb_in_gp = len(group.split('\n'))
    group = re.sub('\n','',group)
    group = [g for g in group]
    uniq, count = np.unique(group, return_counts = True)
    filtre = count==nb_in_gp
    summ += np.sum(filtre)
    #print(group, nb_in_gp, count,filtre,np.sum(filtre))
print('For part 2, the sum is :',summ)