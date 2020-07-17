#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jul 16 12:08:50 2020

@author: vm and gm
"""

from collections import defaultdict
import os

compress_dict = defaultdict(int)

def gen_dict():
    global total_dict
    rootdir = os.getcwd()
    for subdir, dirs, files in os.walk(rootdir):
        for file in files:
            name = file.split(".txt")[0]
            if file.endswith(".txt") and "report" in name:
                obj = open(file,"r")
                lines = obj.readlines()[1:]
                for line in lines:
                    line = line.rstrip().split("-->")
                    val = eval(line[2])
                    compress_dict[val[0]] += val[1]
    final_dict = sorted(compress_dict.items(),key=lambda x: x[1],reverse=True)
    report = open("routetotal.txt", 'w')
    for i in final_dict:
        report.write(str(i)+'\n')
    report.close()      
    obj.close()
                
if __name__ == '__main__':
    gen_dict()