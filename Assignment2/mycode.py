import pandas as pd

#reading the excel file to a variable myexcel
myexcel = pd.ExcelFile('assign2.xlsx')

#exporting the 10 sheets of the myexcel xlsx file to 10 separate csv files
myexcel.parse('countries').to_csv('countries.csv')
myexcel.parse('students').to_csv('students.csv')
myexcel.parse('colors').to_csv('colors.csv')
myexcel.parse('movies').to_csv('movies.csv')
myexcel.parse('smartphones').to_csv('smartphones.csv')
myexcel.parse('banks').to_csv('banks.csv')
myexcel.parse('unitcodes').to_csv('unitcodes.csv')
myexcel.parse('houses').to_csv('houses.csv')
myexcel.parse('pets').to_csv('pets.csv')
myexcel.parse('schools').to_csv('schools.csv')

