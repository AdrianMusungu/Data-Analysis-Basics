import pandas as pd
from pandas import DataFrame
from pandas import read_html
#add the lxml package

#specify the url
url = "https://countrycode.org/"
#creates a list of tables present in the url
dflist = pd.io.html.read_html(url)

#selects the 1st table, index 0
dframe = dflist[0]

print dframe

#prints the column names
#print dframe.columns.values