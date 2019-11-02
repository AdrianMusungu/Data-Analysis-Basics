import pandas as pd

#download xlrd package
#download openpyxl package

#csv can have only one sheet of data, whereas excel can have more than one sheet

#function for reading excel files
excelfile = pd.ExcelFile('demo2.xlsx')
#this is used to parse specific sheets in the excel file, since it can have more than one sheet
dframe = excelfile.parse('demo2')
print dframe
#OR print excelfile.parse('demo2')

