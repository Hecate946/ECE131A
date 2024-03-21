import numpy as np
import matplotlib.pyplot as plt

# Load data from 'data.txt'
data = np.loadtxt("data.txt")

# Calculate sample mean and sample variance
mean_data = np.sum(data) / 100_000
var_data = np.sum([(x - mean_data) ** 2 for x in data]) / 100000

# Plot histogram of the data
plt.figure(figsize=(10, 6))
plt.hist(data, bins=50, density=True, label="Histogram")

# Plot Gaussian PDF with mean and variance of the data
x = np.linspace(np.min(data), np.max(data), 1000)
pdf = (
    1 / np.sqrt(2 * np.pi * var_data) * np.exp(-((x - mean_data) ** 2) / (2 * var_data))
)
plt.plot(x, pdf, color="red", linewidth=2, label="Gaussian PDF")

plt.xlabel("Value")
plt.ylabel("Density")
plt.title("Histogram and Gaussian PDF of the data")
plt.legend()
plt.grid(True)

plt.savefig("./images/q2c.png")
