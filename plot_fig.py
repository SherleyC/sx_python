# -*- coding: utf-8 -*-
"""
Created on Thu Sep  3 23:02:22 2020

@author: csy
"""

import os
import sys

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

    
def plot_img(data_dict, fig_title):
    plt.figure(figsize=(12, 8), dpi=500) 
    plt.title(fig_title, fontsize=16)
    plt.ylabel('y', fontsize=16)
    plt.xlabel('x', fontsize=16)
    plt.xticks(fontsize=16)
    plt.yticks(fontsize=16)
    for name, data_list in data_dict.items():
        length = list(range(len(data_list)))
        plt.scatter(length, data_list, label=name)
    plt.legend() # 显示图例
    plt.savefig(fig_title+'.png')
    plt.close()
        

if __name__ == '__main__':
    csv_path = 'test.csv'
    
    df = pd.read_csv(csv_path, usecols=['temp1', 'depth'])
    df['error'] = (df['temp1']- df['depth'])/df['depth']
    
    test_1_dict = dict()
    test_1_dict['temp1'] = df['temp1'].values.tolist()
    test_1_dict['depth'] = df['depth'].values.tolist()
    plot_img(test_1_dict, 'test_1')
    