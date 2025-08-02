import matplotlib.pyplot as plt
import numpy as np

# Data
lambdas = [128, 192, 256]
labels = [r'$p$', r'$q$', r'$\alpha$',  r'$sk_h$']
#r'$\delta$', r'$\xi$', r'$\nu$', r'$\chi$',
data = [
    [384, 512, 512],  # p_bits
    [128, 192, 256],  # q_bits
    [381, 509, 509],  # alpha_bits
   # [125, 191, 251],   delta_bits
   # [127, 190, 254],  # xi_bits
   # [384, 512, 512],  # nu_bits
   # [383, 511, 511],  # chi_bits
    [382, 510, 510],  # skh_bits
]

# Convert to numpy array for easier plotting
data = np.array(data)

x = np.arange(len(lambdas))  # positions for λ=128,192,256
width = 0.09  # width of each bar

plt.figure(figsize=(12,6))

# Plot each key component as a set of bars
for i in range(len(labels)):
    plt.bar(x + (i - len(labels)/2)*width + width/2, data[i], width=width, label=labels[i])

plt.xticks(x, [r'$\lambda$=128', r'$\lambda$=192', r'$\lambda$=256'])
plt.ylabel("Key size (bits)")
plt.title("Effect of security parameter $\lambda$ on key sizes (bits)")
plt.legend(title="Key components", bbox_to_anchor=(1.05, 1), loc='upper left')
plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.tight_layout()
plt.show()
