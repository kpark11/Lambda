# -*- coding: utf-8 -*-
"""
Created on Fri Oct  1 17:15:15 2021

@author: Student
"""

import numpy as np
import pandas as pd
import os

############## BE CAREFUL WITH THIS. IT WILL WRITE ON THE ACTUAL FILE ################


file = r'C:\Users\Student\OneDrive - University of Tennessee\Desktop\Research\CrPS4\10.8.2021'
os.chdir(file)
cwd = os.getcwd()
print(cwd)
list = os.listdir(file)
print(list)



###### Gotta delete the data descriptions so that pure data can be read ###########
for k in range(len(list)):
    file = open(list[k],"r")
    lines = file.readlines()
    file.close()
    
    del lines[:90]
    
    new_file = open(list[k],"w+")
    
    for line in lines:
        new_file.write(line)
    
    new_file.close()
    
######## Turning wavelength to frequencies and energies #######
for k in range(len(list)):
    data = np.loadtxt(list[k])
    print(data)
    wavelength = data[:,0]
    print(wavelength)
    frequency = (1/wavelength[:])*1e7
    print(frequency)
    energy = frequency/8065.548
    print(energy)
    percent = data[:,1]/100
    data = np.column_stack((data,energy))
    data = np.column_stack((data,frequency))
    data = np.column_stack((data,percent))
    
    df = pd.DataFrame(data, columns = ['Wavelength','Siganl','Energy','Frequency','Signal in percentage'])
    name = list[k]
    new_name = "python_" + list[k]
    print(new_name)
    df.to_csv(new_name,index=False)
        