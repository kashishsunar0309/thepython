# Exercise 15-6: Two D8s Roll
# Throw eight-sided dice 1,000 times and visualize the result using Matplotlib.

import matplotlib.pyplot as plt
from random import randint
from collections import Counter

class Die:
    def __init__(self, num_sides):
        self.num_sides = num_sides

    def roll(self):
        return randint(1, self.num_sides)

# Simulation
die_1 = Die(8)
die_2 = Die(8)
num_rolls = 1_000

results = [die_1.roll() + die_2.roll() for _ in range(num_rolls)]

# Count frequencies efficiently
counter = Counter(results)
x_values = list(range(2, die_1.num_sides + die_2.num_sides + 1))
frequencies = [counter[value] for value in x_values]

# Plot
plt.style.use("seaborn-v0_8")
fig, ax = plt.subplots(figsize=(10, 6))
ax.bar(x_values, frequencies, color="steelblue", edgecolor="white", linewidth=0.5)

ax.set_title(f"Result of Rolling Two D8 Dice {num_rolls:,} Times", fontsize=16)
ax.set_xlabel("Result", fontsize=14)
ax.set_ylabel("Frequency", fontsize=14)
ax.set_xticks(x_values)

plt.tight_layout()
plt.savefig("ex15_6_two_d8.png", dpi=150)
plt.show()
