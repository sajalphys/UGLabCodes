import matplotlib.pyplot as plt
import numpy as np

# Load data from LD.dat file
data = np.loadtxt("LD.dat")  # Replace "LD.dat" with your actual file path

# Extract load and depression data
load = data[:, 0]  # Assuming load is in the first column
depression = data[:, 1]  # Assuming depression is in the second column

# Perform least squares fitting
m, c = np.polyfit(load, depression, 1)

# Generate fitted line points
x_fit = np.linspace(min(load), max(load), 100)
y_fit = m * x_fit + c

# Calculate equation parameters in latex format
equation = r"$y = {0:.4f} + {1:.4f}x$".format(c, m)

# Create the figure and main axes
fig, ax = plt.subplots()

# Plot data and fitted line
ax.plot(load, depression, 'o', label='Data')
ax.plot(x_fit, y_fit, '-', label='Fitted Line')

# Add labels and title
ax.set_xlabel('Load (N)')
ax.set_ylabel('Depression (mm)')
ax.set_title('Least Squares Fitting of Load vs. Depression')

# Create inset axes and position it in the upper middle
ax_inset = fig.add_axes([0.5, 0.8, 0.2, 0.2])  # Adjust width and height as needed

# Plot equation in the inset axes
ax_inset.text(0.5, 0.5, equation, ha='center', va='center', fontsize=10)

# Remove axes, ticks, and labels from the inset axes
ax_inset.axis('off')

# Add legend to the main axes
ax.legend(loc='best')

# Adjust layout and show the plot
plt.tight_layout()
plt.show()

