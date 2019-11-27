# -*- coding: utf-8 -*-
"""
Created on Tue Nov 26 12:22:45 2019

@author: Guo
"""

import os
import shutil

path = './my_faces'
full_path = 'C:\\Users\\Administrator\\Desktop\\aaaa\\my_faces\\'

file_list = os.listdir(path)

for one_file in file_list:
    file_full_name = one_file
    point = '.'
    file_name = file_full_name[:file_full_name.index(point)]
    new_name = int(file_name) + 4000
    new_file_full_name = str(new_name) + '.jpg'
    #print(full_path + file_full_name)
    shutil.copy(full_path + file_full_name, full_path + new_file_full_name)