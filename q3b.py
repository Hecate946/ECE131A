import pandas as pd
import matplotlib.pyplot as plt

# Load the dataset
data = pd.read_csv("user_data.csv")

# Separate the data for bought and not bought
bought_data = data[data["Bought"] == 1]
not_bought_data = data[data["Bought"] == 0]

# Calculate the conditional fractions for each realization
t_pmf_b1 = bought_data["Spender Type"].value_counts(normalize=True).sort_index()
t_pmf_b0 = not_bought_data["Spender Type"].value_counts(normalize=True).sort_index()

s_pmf_b1 = bought_data["Sex"].value_counts(normalize=True).sort_index()
s_pmf_b0 = not_bought_data["Sex"].value_counts(normalize=True).sort_index()

a_pmf_b1 = bought_data["Age"].value_counts(normalize=True).sort_index()
a_pmf_b0 = not_bought_data["Age"].value_counts(normalize=True).sort_index()

# Plot the conditional PMFs separately
fig, axs = plt.subplots(2, 3, figsize=(18, 12))

# First row
axs[0, 0].bar(t_pmf_b1.index, t_pmf_b1.values, label="Bought")
axs[0, 0].set_xlabel("Type of Spender")
axs[0, 0].set_ylabel("Probability")
axs[0, 0].set_title("Conditional PMF of Type of Spender given Bought Status")
axs[0, 0].legend()

axs[0, 1].bar(s_pmf_b1.index, s_pmf_b1.values, label="Bought")
axs[0, 1].set_xlabel("Sex")
axs[0, 1].set_ylabel("Probability")
axs[0, 1].set_title("Conditional PMF of Sex given Bought Status")
axs[0, 1].legend()

axs[0, 2].bar(a_pmf_b1.index, a_pmf_b1.values, label="Bought")
axs[0, 2].set_xlabel("Age")
axs[0, 2].set_ylabel("Probability")
axs[0, 2].set_title("Conditional PMF of Age given Bought Status")
axs[0, 2].legend()

# Second row
axs[1, 0].bar(t_pmf_b0.index, t_pmf_b0.values, label="Not Bought")
axs[1, 0].set_xlabel("Type of Spender")
axs[1, 0].set_ylabel("Probability")
axs[1, 0].set_title("Conditional PMF of Type of Spender given Not Bought Status")
axs[1, 0].legend()

axs[1, 1].bar(s_pmf_b0.index, s_pmf_b0.values, label="Not Bought")
axs[1, 1].set_xlabel("Sex")
axs[1, 1].set_ylabel("Probability")
axs[1, 1].set_title("Conditional PMF of Sex given Not Bought Status")
axs[1, 1].legend()

axs[1, 2].bar(a_pmf_b0.index, a_pmf_b0.values, label="Not Bought")
axs[1, 2].set_xlabel("Age")
axs[1, 2].set_ylabel("Probability")
axs[1, 2].set_title("Conditional PMF of Age given Not Bought Status")
axs[1, 2].legend()

plt.tight_layout()
plt.savefig("./images/q3b.png")
