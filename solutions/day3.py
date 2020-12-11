import pandas as pd
import numpy as np

root_dir = '/Users/jeremynadal/Documents/adventofcode/adventofcode2020/'
file_path = root_dir + 'inputs/input_3.txt'

with open(file_path,"r") as infile:
    data =  np.matrix([list(line.strip()) for line in infile.readlines()])
    
print('data is of shape :',data.shape,'\n')


mult = 1
directions = [[1,1],[1,3],[1,5],[1,7],[2,1]] # One down and three right

for direction in directions : 
    print('For direction :',direction)
    pos = [0,0]
    trees = 0
    while pos[0] < (data.shape[0]-1) : 
        pos[0] += direction[0]
        pos[1] += direction[1]
        if pos[1] >= data.shape[1]:
            pos[1] = pos[1] - data.shape[1]
        if data[pos[0],pos[1]] == '#':
            trees += 1
    mult *= trees
        
    print('Final position is ',pos,'we hit {} trees\n'.format(trees))
    
print('The multiplication of all the hits is :',mult,'\n')