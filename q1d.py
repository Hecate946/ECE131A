import random

t_values = [50, 100, 1000, 2000, 3000, 10000, 100000]


def simulate_die_tosses(tosses):
    primes = [2, 3, 5, 7, 11]  # Prime numbers on a 12-sided die

    odd_count = 0
    for _ in range(tosses):
        roll = random.randint(1, 17)
        result = random.choice(primes) if roll > 12 else roll
        if result % 2 != 0:
            odd_count += 1
    return odd_count / tosses


for t in t_values:
    estimated_probability = simulate_die_tosses(t)
    percent = estimated_probability * 100
    print(f"Probability of getting an odd number for {t} tosses: {percent:.2f}%")
