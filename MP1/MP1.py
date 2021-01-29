#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jan 28 15:10:07 2021

@author: dingyishang
"""

"""
 Output
 You need to implement the Apriori algorithm and use it to mine category sets that are frequent in the input data. When implementing the Apriori algorithm, you may use any programming language you like. We only need your result pattern file, not your source code file.

 After implementing the Apriori algorithm, please set the relative minimum support to 0.01 and run it on the 77,185 category lists. In other words, you need to extract all the category sets that have an absolute support larger than 771.

 Part 1

 Please output all the length-1 frequent categories with their absolute supports into a text file named "patterns.txt". Every line corresponds to exactly one frequent category and should be in the following format:

 support:category

 For example, suppose a category (Fast Food) has an absolute support 3000, then the line corresponding to this frequent category set in "patterns.txt" should be:

 3000:Fast Food
"""

#--------------------------------------------------#    
with open("categories.txt", "r") as f:
    content = f.readlines()

# remove whitespace characters like `\n` at the end of each line AND split items by semicolon
content = [x.strip() for x in content] 
content = [x.split(";") for x in content] 

list_entry=[]  
for i in range(0,len(content)):
    list_entry += content[i]



freq1 = {}
for item in list_entry:
    if (item in freq1):
        freq1[item] += 1
    else:
        freq1[item] = 1

freq1_reduced = {k:v for (k,v) in freq1.items() if v>771}


with open('patterns.txt', 'w') as f:
    for key, value in freq1_reduced.items():
     print(str(value)+':'+str(key),file=f)

    
#finish in 0.4065 seconds   
 
"""     
 Part 2

 Please write all the frequent category sets along with their absolute supports into a text file named "patterns.txt". Every line corresponds to exactly one frequent category set and should be in the following format:

 support:category_1;category_2;category_3;...

 For example, suppose a category set (Fast Food; Restaurants) has an absolute support 2851, then the line corresponding to this frequent category set in "patterns.txt" should be:

 2851:Fast Food;Restaurants
"""
#--------------------------------------------------# 
#2 item frequent sets
from itertools import combinations 

comb2 = list(combinations(list(freq1_reduced.keys()),2)) 

freq2 = {}
for i in range(0,len(comb2)):
    for j in range(0,len(content)):
        #To check if the first list (big) contains ALL elements in the second list (small)
        if (all(elem in content[j] for elem in list(comb2[i]))):
            if comb2[i] in freq2:
                freq2[comb2[i]] += 1  
            else:
                freq2[comb2[i]] = 1

freq2_reduced = {k:v for (k,v) in freq2.items() if v>771}


with open('patterns.txt', 'a') as f:
    for key, value in freq2_reduced.items():
       print(str(value)+':'+str(';'.join(key)),file=f)

#finish in 78.9789 seconds

#--------------------------------------------------#
#3 item frequent sets
import time
tic = time.perf_counter()
freq2_reduced_list = [item for t in list(freq2_reduced.keys()) for item in t]
comb3 = list(combinations(set(freq2_reduced_list),3)) 


freq3 = {}
for i in range(0,len(list(comb3))):
    ind=0
    for j in range(0,len(list(freq2_reduced.keys()))):
        if all(elem in comb3[i] for elem in list(freq2_reduced.keys())[j]):
            ind += 1
    if ind==3:
        for k in range(0,len(content)):
            if (all(elem in content[k] for elem in list(comb3[i]))):
                if comb3[i] in freq3:
                    freq3[comb3[i]] += 1
                else:
                    freq3[comb3[i]] = 1

freq3_reduced = {k:v for (k,v) in freq3.items() if v>771}


with open('patterns.txt', 'a') as f:
    for key, value in freq3_reduced.items():
       print(str(value)+':'+str(';'.join(key)),file=f)

#finish in 1.2330 seconds

#--------------------------------------------------#
#4 item frequent sets

freq3_reduced_list = [item for t in list(freq3_reduced.keys()) for item in t]
comb4 = list(combinations(set(freq3_reduced_list),4)) 


freq4 = {}
for i in range(0,len(list(comb4))):
    ind=0
    for j in range(0,len(list(freq2_reduced.keys()))):
        if all(elem in comb4[i] for elem in list(freq2_reduced.keys())[j]):
            ind += 1
    if ind==4:
        for k in range(0,len(content)):
            if (all(elem in content[k] for elem in list(comb4[i]))):
                if comb4[i] in freq4:
                    freq4[comb4[i]] += 1
                else:
                    freq4[comb4[i]] = 1

freq4_reduced = {k:v for (k,v) in freq4.items() if v>771}

freq4_reduced=={}
#True so stop