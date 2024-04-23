import pandas as pd
import numpy as np
import json

# Load the JSON data
with open(r"C:\Users\venki\Work\scrapy_data_project_app\myproject\final_recipes.json", 'r', encoding='utf-8') as file:
    data = json.load(file)

# Extract 'receipe_data' into a DataFrame
df = pd.DataFrame(data["receipe_data"])

# Check if "Prep Time" and "Cook Time" columns exist
if "Prep Time" in df.columns and "Cook Time" in df.columns:
    df["Prep Time"] = df["Prep Time"].str.replace("\u00bd", "").str.replace("\u00bc", "")
    df["Cook Time"] = df["Cook Time"].str.replace("\u00bd", "").str.replace("\u00bc", "")

    # Calculate the median and interquartile range (IQR) for "Prep Time" with non-empty values
    prep_time_values = df["Prep Time"][df["Prep Time"] != ""].apply(lambda x: int(x.split()[0]))
    q1 = prep_time_values.quantile(0.25)
    q3 = prep_time_values.quantile(0.75)

    # Function to generate a random integer value within the IQR range
    def generate_random_prep_time():
        return f"{int(np.random.uniform(q1, q3))} minutes"

    # Generate a single random value for all empty "Prep Time" entries
    random_prep_time = generate_random_prep_time()

    # Update "Prep Time" with the same random value for all rows where it is empty
    for index, row in df.iterrows():
        if row["Prep Time"] == "":
            df.at[index, "Prep Time"] = random_prep_time

    # Calculate total time (Prep Time + Cook Time)
    df["Total Time"] = df.apply(lambda row: f"{int(row['Prep Time'].split()[0]) + int(row['Cook Time'].split()[0]) if row['Cook Time'] != '' else int(row['Prep Time'].split()[0])} minutes", axis=1)

    # Remove "\u00bd" characters from all columns
    df = df.replace(to_replace=["\u00bd", "\u00bc"], value="", regex=True)

    # Create the updated JSON structure
    updated_data = {
        "code": 200,
        "status": "Success",
        "Message": "Successfully Fetched the Recipes List",
        "recipe_data": df.to_dict(orient="records")
    }

    # Save the updated JSON to a new file
    with open("updated_recipes_1.json", "w") as outfile:
        json.dump(updated_data, outfile, indent=4)

    print("Updated JSON data saved to 'updated_recipes.json'.")
else:
    print("'Prep Time' or 'Cook Time' column not found in the DataFrame.")
