import pandas as pd

# Read the Excel file into a DataFrame
df = pd.read_excel('dataset.xlsx')

# Interpolate missing values using linear interpolation
df['Population (millions)'].interpolate(method='linear', inplace=True)

# Save the DataFrame back to the same Excel file
#df.to_excel('dataset.xlsx', index=False)
print(df.to_string())