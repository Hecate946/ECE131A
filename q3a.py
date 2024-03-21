import pandas as pd
import matplotlib.pyplot as plt

# Load the dataset
data = pd.read_csv("user_data.csv")

# Calculate the fractions for each realization
b_pmf = data["Bought"].value_counts(normalize=True).sort_index()
t_pmf = data["Spender Type"].value_counts(normalize=True).sort_index()
s_pmf = data["Sex"].value_counts(normalize=True).sort_index()
a_pmf = data["Age"].value_counts(normalize=True).sort_index()
print(b_pmf)
print(t_pmf)
print(s_pmf)
print(a_pmf)

# Plot the PMFs
plt.figure(figsize=(12, 8))

plt.subplot(2, 2, 1)
plt.bar(b_pmf.index, b_pmf.values)
plt.xlabel("Bought Status")
plt.ylabel("Probability")
plt.title("PMF of Bought Status")

plt.subplot(2, 2, 2)
plt.bar(t_pmf.index, t_pmf.values)
plt.xlabel("Type of Spender")
plt.ylabel("Probability")
plt.title("PMF of Type of Spender")

plt.subplot(2, 2, 3)
plt.bar(s_pmf.index, s_pmf.values)
plt.xlabel("Sex")
plt.ylabel("Probability")
plt.title("PMF of Sex")

plt.subplot(2, 2, 4)
plt.bar(a_pmf.index, a_pmf.values)
plt.xlabel("Age")
plt.ylabel("Probability")
plt.title("PMF of Age")

plt.tight_layout()
plt.savefig("./images/q3a.png")
