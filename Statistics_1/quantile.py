import pandas as pd
import json
import re

# Load the original JSON file into a pandas DataFrame
with open('final_mushroom_recipes.json', 'r') as file:
    data = json.load(file)

# Access the "recipe data" from the JSON
recipe_data = data.get('recipe_data', [])

# Create the initial DataFrame
df = pd.DataFrame(recipe_data)

# Print out the column names to check for the correct column name
print("Original Column Names:", df.columns)

# Extract numeric part from "Prep Time" and convert to numeric
prep_time_column_name = 'Prep Time'  # Update with the correct column name
if prep_time_column_name in df.columns:
    df[prep_time_column_name] = df[prep_time_column_name].str.extract('(\d+)').astype(float)

    # Calculate quantiles, ignoring NaN values
    quantiles = df[prep_time_column_name].quantile([0.25, 0.5, 0.75])

    # Define a function to fill empty values with quantiles and round to whole number
    def fill_with_quantile(value):
        if pd.isnull(value):
            return round(quantiles[0.5])  # Fill with rounded median if NaN
        return round(value)

    # Apply the function to the "Prep Time" column
    df[prep_time_column_name] = df[prep_time_column_name].apply(fill_with_quantile)

    # Add "minutes" to the "Prep Time" values
    df[prep_time_column_name] = df[prep_time_column_name].astype(str) + " minutes"

else:
    print(f"Column '{prep_time_column_name}' not found in DataFrame.")

# Convert column names to lowercase and remove spaces
df.columns = df.columns.str.lower().str.replace(' ', '')

# Print out the updated column names
print("Updated Column Names:", df.columns)

# Define a function to convert time strings to minutes
def convert_to_minutes(time_str):
    if time_str == "":
        return 0
    # Remove " minutes" from the string and convert to integer
    return int(time_str.replace(" minutes", ""))

# Convert "preptime" and "cooktime" columns to minutes
df['preptime'] = df['preptime'].apply(convert_to_minutes)
df['cooktime'] = df['cooktime'].apply(convert_to_minutes)

# Update "cooktime" for recipes with missing values
df['cooktime'] = df.apply(lambda row: row['preptime'] if row['cooktime'] == 0 else row['cooktime'], axis=1)

# Calculate "totaltime" by adding "preptime" and "cooktime" (in minutes)
df['totaltime'] = df['preptime'] + df['cooktime']

# Convert "preptime", "cooktime", and "totaltime" back to string format with " minutes"
df['preptime'] = df['preptime'].astype(str) + " minutes"
df['cooktime'] = df['cooktime'].astype(str) + " minutes"
df['totaltime'] = df['totaltime'].astype(str) + " minutes"

# Convert DataFrame back to JSON format
updated_data = df.to_dict(orient='records')

# Create the updated JSON structure
updated_json = {
    "code": 200,
    "message": "Successfully fetched the data",
    "status": "Success",
    "recipe data": updated_data
}

# Write the updated JSON back to file with ensure_ascii=False
with open('updated_mushroom_recipes.json', 'w', encoding='utf-8') as file:
    json.dump(updated_json, file, indent=4, ensure_ascii=False)

