import pandas as pd

# Read the CSV files
file1 = '/users/axel22/dropbox/trade_data/dac/csv/3316574_DutchAtlantic_accdb/DutchAtlantic.accdb.JLogfinal.csv'
file2 = '/users/axel22/dropbox/trade_data/dac/csv/3316574_DutchAtlantic_accdb/DutchAtlantic.accdb.migrants.csv'

df1 = pd.read_csv(file1)
df2 = pd.read_csv(file2)

# merge the dataframes based on "JourneylogID"
result = pd.merge(df1, df2, on='JourneylogID')

# Save the result to a new CSV file
result.to_csv('/users/axel22/documents/trade project/data harmonisation/copies of raw data csv files/jlogfinal+migrants.csv', index=False)
