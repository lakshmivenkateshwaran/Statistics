import matplotlib.pyplot as plt
import latexify

# Decorate the functions with latexify
@latexify.function
def step1():
    return r'To interpolate a value $y$ at a point $x$ between two known points $(x_1, y_1)$ and $(x_2, y_2)$:'

@latexify.function
def step2():
    return r'Calculate the y-intercept ($b$): $b = y_1 - m \times x_1$'

@latexify.function
def step3():
    return r'Interpolate the value $y$ at the point $x$ using the equation of the line: $y = mx + b$'

# Generate LaTeX representations for each step
latex_step1 = step1()
latex_step2 = step2()
latex_step3 = step3()

# Set up Matplotlib figure and axes
fig, ax = plt.subplots()

# Add text with the LaTeX formulas
ax.text(0.1, 0.8, latex_step1, fontsize=12, color='black', ha='left', va='top')
ax.text(0.1, 0.5, r'Calculate the slope ($m$):', fontsize=12, color='black', ha='left', va='top')
ax.text(0.2, 0.3, r'$m = \frac{{y_2 - y_1}}{{x_2 - x_1}}$', fontsize=12, color='black', ha='left', va='bottom')
ax.text(0.1, 0.2, latex_step2, fontsize=12, color='black', ha='left', va='top')
ax.text(0.1, 0.1, latex_step3, fontsize=12, color='black', ha='left', va='top')

# Customize background color of the figure
fig.patch.set_facecolor('lightblue')

# Hide axes
ax.axis('off')

# Show the plot
plt.show()
