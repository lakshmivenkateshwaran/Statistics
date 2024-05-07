## Linear Interpolation Visualization
This Python script demonstrates the process of linear interpolation using Matplotlib for visualization and LaTeX formatting for mathematical notation.

## Description
The script uses Matplotlib to create a visualization of the steps involved in linear interpolation. It explains the process through a series of annotated steps using LaTeX-formatted equations.

## Dependencies
Python 3.x
Pandas
Matplotlib
Latexify

## Install dependencies using:

pip install matplotlib latexify

## Usage
 - Run the Python script latex_updated.py.
 - The script will display a plot illustrating the steps of linear interpolation.
 - Each step is annotated with LaTeX-formatted equations explaining the process.

## Sample Dataset

Refer the dataset.xlsx file. In which you can see the NaN values for some rows. We are calculating the respective 

## Values
- x1 = 2008
- y1 = 3.3
- x2 = 2012
- y2 = 3.4

## For 2010:
- The nearest recorded population values are for the years 2008 (3.3 million) and 2012 (3.4 million).
- We'll use linear interpolation between these two points to estimate the population for 2010.
## For 2018:
- The nearest recorded population values are for the years 2016 (3.5 million) and 2014 (3.45 million).
- We'll use linear interpolation between these two points to estimate the population for 2018.
## For 2020:
- The nearest recorded population values are for the years 2018 and 2016.
- We'll use linear interpolation between these two points to estimate the population for 2020.

**Now you can apply these values with the steps that you got from resulted matplotlib graph**

## Folder Structure
- latex_updated.py   # Show you the steps involved in Linear interpolation
- main.py  # Code implementation of Linear interpolation
- dataset.xlsx  # Sample data for calculating Linear interpolation