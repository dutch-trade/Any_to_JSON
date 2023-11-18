import pandas as pd

# Read the CSV files
file1 = '/users/axel22/documents/trade project/data harmonisation/copies of raw data csv files/JLog+migrants+cargo.csv'
file2 = '/users/axel22/dropbox/trade_data/dac/csv/3316574_DutchAtlantic_accdb/DutchAtlantic.accdb.destination.csv'

df1 = pd.read_csv(file1)
df2 = pd.read_csv(file2)

# Specify the columns to merge on
left_on_column = 'Place'  # Column in the first file
right_on_column = 'DestinationID'  # Column in the second file

# merge the dataframes based on "JourneylogID"
result = pd.merge(df1, df2, left_on=left_on_column, right_on=right_on_column,how='left')

# Save the result to a new CSV file
result.to_csv('/users/axel22/documents/trade project/data harmonisation/copies of raw data csv files/Jlog+migrants+cargo+destinations.csv', index=False)
