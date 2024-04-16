## Data Transformation

This Python script provides a streamlined approach to transform data stored in a JSON file. Using the powerful pandas library, the script loads the original recipe data, cleans 'Prep Time' values, calculates 'Cook Time', and creates a new 'Total Time' column. The final transformed data is then exported back to a JSON format for easy handling and analysis.

## Setup

1. Clone the repository:
   git clone https://github.com/your-username/Recipes_Scraper

2. Install dependencies
   pip install -r requirements.txt

## Steps

## Load Original Recipe Data
The script begins by loading the original recipe data from a JSON file into a pandas DataFrame.

## Check and Clean 'Prep Time' Values
'Prep Time' values are checked and cleaned to ensure accurate cooking durations. The script extracts the numeric part of each 'Prep Time' entry, standardizing the format.

## Calculate and Add 'Cook Time'
The script calculates the 'Cook Time' for each recipe, essential for understanding the total cooking time. 'Cook Time' is added to the DataFrame.

## Create 'Total Time' Column
By summing 'Prep Time' and 'Cook Time', the script creates a new 'Total Time' column, providing a comprehensive view of the entire cooking process for each recipe.

## Export Transformed Data to JSON
The final step involves exporting the transformed DataFrame back to a JSON format, ensuring seamless data handling and sharing.

## Folder Structure

- Quantile.py                    # Python script transform "Prep Time" Value using Quantile
- requirements.txt               # List of project dependencies
- final_mushroom_recipes.json    # File which has empty value in "Prep Time" and "Total Time" (Line 634 and 636)
- updated_mushroom_recipes.json  # Updated file with the values (Line 634 and 636)

## Usage

- Ensure you have Python installed on your system.
- Install the required libraries using pip install -r requirements.txt.
- Run the script quantile.py to execute the data transformation.
- The transformed data will be saved to updated_mushroom_recipes.json.
