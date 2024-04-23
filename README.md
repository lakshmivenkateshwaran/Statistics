## Data Transformation

This Python script provides a streamlined approach to transform data stored in a JSON file. Using the powerful pandas library, the script loads the original recipe data, cleans 'Prep Time' values, calculates 'Cook Time', and creates a new 'Total Time' column. The final transformed data is then exported back to a JSON format for easy handling and analysis.

## Setup

1. Clone the repository:
   git clone https://github.com/your-username/Recipes_Scraper

2. Install dependencies
   pip install -r requirements.txt

## Steps

1. Data Import: Load recipe data from JSON files.
2. DataFrame Setup: Convert JSON data into a structured DataFrame.
3. Cleanse & Enhance: Remove special characters and calculate total time.
4. Data Augmentation: Add 'Total Time' column for easier analysis.
5. Serialization & Integration: Save enriched dataset back to JSON for seamless use.

## Folder Structure

- iqr.py                         # Python script transform "Prep Time" Value using Quantile
- requirements.txt               # List of project dependencies
- final_recipes.json             # File which has empty value in "Prep Time" and "Total Time" (Line 634 and 636)
- updated_recipes.json           # Updated file with the values 

## Usage

- Ensure you have Python installed on your system.
- Install the required libraries using pip install -r requirements.txt.
- Run the script iqr.py to execute the data transformation.
- The transformed data will be saved to updated_recipes_1.json.
