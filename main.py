import pandas as pd
import matplotlib.pyplot as plt

# Read the CSV file
df = pd.read_csv("SOCR-HeightWeight.csv", index_col='Index')

# Calculate the mean of the 'height' and 'weight' columns
mean_height = df['Height(Inches)'].mean()
mean_weight = df['Weight(Pounds)'].mean()

# Calculate the standard deviation
std_height = df['Height(Inches)'].std().round(0)
std_weight = df['Weight(Pounds)'].std().round(0)

# Calculate and round the z-scores for 'height' and 'weight' columns
z_score_height = ((df['Height(Inches)'] - mean_height) / std_height).round(2)
z_score_weight = ((df['Weight(Pounds)'] - mean_weight) / std_weight).round(2)

# Print the result
print(f"The standard deviation of the 'Height' column is: {std_height}")
print(f"The standard deviation of the 'Weight' column is: {std_weight}")

# Display the z-scores
print("Z-scores for 'height' column:")
print(z_score_height)
print("\nZ-scores for 'weight' column:")
print(z_score_weight)

# Check if there are any missing values
has_missing_values = df.isnull().values.any()

# Print the result
print(has_missing_values)

# Create a histogram visualization for 'height' z-scores
plt.figure(figsize=(10, 6))
plt.hist(z_score_height.dropna(), bins=10, color='skyblue', edgecolor='black')
plt.title('Histogram of Z-Scores for Height')
plt.xlabel('Z-Score')
plt.ylabel('Frequency')
plt.grid(True)
plt.show()

# Create a histogram visualization for 'weight' z-scores
plt.figure(figsize=(10, 6))
plt.hist(z_score_weight.dropna(), bins=10, color='lightgreen', edgecolor='black')
plt.title('Histogram of Z-Scores for Weight')
plt.xlabel('Z-Score')
plt.ylabel('Frequency')
plt.grid(True)
plt.show()


