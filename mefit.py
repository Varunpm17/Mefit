#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jun 16 13:53:53 2020

@author: gauravmohan

"""

from collections import defaultdict
import pandas as pd
import os



count = 0


def route():
    global count 
    rootdir = os.getcwd()
    for subdir, dirs, files in os.walk(rootdir):
        for file in files:
            filepath = subdir + os.sep + file
            name = file.split(".csv")[0]
            if name == "Routes":
                    data3 = pd.read_csv(filepath)
                    rows = len(data3.index)
                    count += 1
            if name == "MeFitGeneralData":
                    data1 = pd.read_csv(filepath)
                    count += 1
            if count == 2:    
                find_file(data3,data1,rows)
    

def find_file(data3,data1,rows):
    rootdir = os.getcwd()
    for subdir, dirs, files in os.walk(rootdir):
        for file in files:
            filepath = subdir + os.sep + file
            if filepath.endswith(".csv"):
                name = file.split(".csv")[0]
                for i in range(0,rows):
                    location = data3.iat[i,0].replace(" ", "")
                    if name == location:         
                        data2 = pd.read_csv(filepath)
                        read_data(data1,data2,location)
                

def read_data(data1, data2, location):
    global count
    initial_dict = {}
    me_data = defaultdict(dict)
    RowCount = len(data1.index)
    RowCount2 = len(data2.index)
    for i in range(0, RowCount2):
        initial_dict[data2.iat[i,1]] = data2.iat[i,2] #initial_dict creates a key of slots to a value of item name
    #print(initial_dict)
    for i in range (0,RowCount):
        for k,v in initial_dict.items(): #initial dict is used to create the inner dictionary
            #if the slot matches from the two data files and the machine number/location are the same as inputted
            #and the slots is alr in me_data then traverse through it and add the item to the nested dictionary
            if data1.iat[i,1] == (str)(k) and data1.iat[i,0] == data2.iat[0,0] and data1.iat[i,1] in me_data[data2.iat[0,0]] and location == data2.iat[1,0]: 
                for slot,item in me_data[data2.iat[0,0]].items():
                    if data1.iat[i,1] == slot:
                        me_data[data1.iat[i,0]][data1.iat[i,1]] = ((item[0],item[1]+1,item[2]+data1.iat[i,2]*data1.iat[i,3],data1.iat[i,4],data1.iat[i,5]))
                        #me_data --> {machine id:{slot info: ((item,count of how many times item has shown up))}}
            elif data1.iat[i,1] == (str)(k) and data1.iat[i,0] == data2.iat[0,0] and location == data2.iat[1,0]:
                me_data[data1.iat[i,0]][data1.iat[i,1]] = ((v,1,data1.iat[i,2]*data1.iat[i,3],data1.iat[i,4],data1.iat[i,5]))
                #if the slot item is not in the inner dictionary then set the freq of the item to 1
    count += 1
    report = open(f"report{count}.txt", 'a')
    report.write(location+'\n')
    for i,j in me_data.items():
        #print(j.items())
        for k,v in j.items():
            report.write(f'{i}-->{k}-->{v}\n')
    report.close()
    
    
       
      

if __name__ == '__main__':
    route()   
    
    
