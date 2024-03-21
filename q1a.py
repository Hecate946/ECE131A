import random

t_values = [50, 100, 1000, 2000, 3000, 10000, 100000]


def simulate_die_tosses(tosses):
    odd_count = 0
    for _ in range(tosses):
        result = random.randint(1, 12)
        if result % 2 != 0:
            odd_count += 1
    return odd_count / tosses


for t in t_values:
    estimated_probability = simulate_die_tosses(t)
    percent = estimated_probability * 100
    print(f"Probability of getting an odd number for {t} tosses: {percent:.2f}%")
