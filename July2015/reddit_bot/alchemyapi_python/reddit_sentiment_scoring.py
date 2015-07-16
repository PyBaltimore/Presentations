# coding: utf-8
import os
import csv
results = {'positive': 0, 'negative':0}
neg = 0
pos = 0
with open('data.csv', 'r') as infile:
    reader = csv.reader(infile, delimiter=',')
    for index,line in enumerate(reader):
        if line[-1] == 'negative':
            results['negative'] += float(line[-2])
            neg += 1 
        else:
            results['positive'] += float(line[-2])
            pos += 1

print results
print pos
print neg
