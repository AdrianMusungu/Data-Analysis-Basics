import pandas as pd
import seaborn as sns

df = pd.read_csv('gapminder-FiveYearData.csv')

#creating the pivot table with x-axes as year and y-axes as continent with life expectancy as the values to be filled within
new_df = pd.pivot_table(df, values='lifeExp', index=['year'], columns='continent')
print new_df

#plotting the heatmap
heatMap = sns.heatmap(new_df)
heatMap.set_title('Assignment 3: Heat Map of Pivot Table by Adrian Musungu')
#saving the heatmap to an image file
heatMap.get_figure().savefig('pivot_heatMap.png')