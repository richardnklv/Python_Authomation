import pandas as pd

medalTable = pd.read_html('https://en.wikipedia.org/wiki/List_of_countries_by_medal_count_at_International_Mathematical_Olympiad')

correct_table = medalTable[0]
# correct_table.set_index('Country', inplace=True)
# print(correct_table)

correct_table.set_index('Rank', inplace=True)

# cleaning Country columns from links and [2]
correct_table['Country'] = correct_table['Country'].str.replace(r"\[.*\]", "", regex=True)

selected_columns = correct_table[['Country', 'Gold', 'Silver', 'Bronze']]

print(selected_columns.head(10))
