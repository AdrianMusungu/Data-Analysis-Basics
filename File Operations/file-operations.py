## OBJECTIVE ##
#importing csv as dataframe
#using readtable of pandas
#reading partial rows of a csv file
#dumping data into a new csv file
#selecting specific columns of a csv file

import numpy as np
import pandas as pd
from pandas import Series, DataFrame

#if you use without 'header=None', the 1st row is automatically considered to be the headers
dframe = pd.read_csv('demo.csv')
print 'dframe:'
print dframe

#with header defined as 'None', then the 1st row is not considered the header row
dframeA = pd.read_csv('demo.csv',header=None)
print 'dframeA:'
print dframeA

dframeB = pd.read_csv('demo1.csv', header=None)
print 'dframeB:'
print dframeB

#ONE CAN ALSO USE read_table(), though it is deprecated

dframe2 = pd.read_table('demo1.csv', sep=',', header=None)
print 'dframe2:'
print dframe2

#importing of partial rows
print 'Partial row selection using nrows=2:'
print pd.read_csv('demo1.csv', header=None, nrows=2)

#dumping dataframe to csv
#if you dont specify separator, it will use comma
dframe2.to_csv('dframe2OUT.csv', sep='!')

#importing of specific columns
dframe2.to_csv('dframeSPColumn.csv', columns=[0,1])
