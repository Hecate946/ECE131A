import pandas as pd

# Load the dataset
data = pd.read_csv("user_data.csv")

# Calculate the probability of B=0 and B=1
p_b0 = len(data[(data["Bought"] == 0)]) / len(data)
p_b1 = len(data[(data["Bought"] == 1)]) / len(data)

# Calculate the probability of T=1 given B=0 and B=1
p_t1_given_b0 = (
    len(data[(data["Bought"] == 0) & (data["Spender Type"] == 1)]) / len(data) / p_b0
)
p_t1_given_b1 = (
    len(data[(data["Bought"] == 1) & (data["Spender Type"] == 1)]) / len(data) / p_b1
)

# Calculate the probability of S=0 given B=0 and B=1
p_s0_given_b0 = len(data[(data["Bought"] == 0) & (data["Sex"] == 0)]) / len(data) / p_b0
p_s0_given_b1 = len(data[(data["Bought"] == 1) & (data["Sex"] == 0)]) / len(data) / p_b1

# Calculate the probability of A<=67 given B=0 and B=1
p_a67_given_b0 = (
    len(data[(data["Bought"] == 0) & (data["Age"] <= 67)]) / len(data) / p_b0
)
p_a67_given_b1 = (
    len(data[(data["Bought"] == 1) & (data["Age"] <= 67)]) / len(data) / p_b1
)

# Calculate the joint probability of B=0, T=1, S=0, and A<=67
p_b0_t1_s0_a67 = p_b0 * p_t1_given_b0 * p_s0_given_b0 * p_a67_given_b0
p_b1_t1_s0_a67 = p_b1 * p_t1_given_b1 * p_s0_given_b1 * p_a67_given_b1


p_t1 = len(data[data["Spender Type"] == 1]) / len(data)
p_s0 = len(data[data["Sex"] == 0]) / len(data)
p_a67 = len(data[data["Age"] <= 67]) / len(data)


p_b0_given_t1_s0_a67 = p_b0_t1_s0_a67 / (p_t1 * p_s0 * p_a67)
p_b1_given_t1_s0_a67 = p_b1_t1_s0_a67 / (p_t1 * p_s0 * p_a67)

print("P(B=0 | T=1, S=0, A<=67):", p_b0_given_t1_s0_a67)
print("P(B=1 | T=1, S=0, A<=67):", p_b1_given_t1_s0_a67)

# Prediction for a female below 67 who is a large spender
# Assuming 'large spender' corresponds to spender type 1
predicted_buy = 1 if p_b1_given_t1_s0_a67 > p_b0_given_t1_s0_a67 else 0
print(
    "Prediction for a female below 67 who is a large spender:",
    "Will buy" if predicted_buy else "Will not buy",
)
