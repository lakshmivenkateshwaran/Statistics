import matplotlib.pyplot as plt

# Text formula for z-score with Greek symbols
text_formula = 'z-score = (x - μ) / σ'

# Plotting
plt.figure(figsize=(8, 6))
plt.text(0.5, 0.5, text_formula, fontsize=18, ha='center', va='center')
plt.axis('off')  # Turn off axis
plt.show()
