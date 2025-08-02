import matplotlib.pyplot as plt
import numpy as np

# Focused data
lambdas = [128, 192, 256]
p_bits = [384, 512, 512]
q_bits = [128, 192, 256]
delta_bits = [125, 191, 251]
xi_bits = [127, 190, 254]

keys = [p_bits, q_bits, delta_bits, xi_bits]
labels = [r'$p$', r'$q$', r'$\delta$', r'$\xi$']

n_groups = len(lambdas)
n_keys = len(labels)
x = np.arange(n_groups)
bar_width = 0.18

plt.figure(figsize=(8,5))

for i, (key_bits, label) in enumerate(zip(keys, labels)):
    plt.bar(x + i*bar_width - (n_keys/2)*bar_width + bar_width/2, key_bits, 
            bar_width, label=label)

plt.xticks(x, [f'λ={l}' for l in lambdas])
plt.xlabel("Security parameter λ")
plt.ylabel("Key size (bits)")
plt.title("Key sizes vs security parameter λ (simplified)")
plt.legend(title="Key components", fontsize=9)
plt.tight_layout()
plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.show()
plt.figure(figsize=(8,5))
plt.plot(lambdas, p_bits, marker='o', label=r'$p$')
plt.plot(lambdas, q_bits, marker='o', label=r'$q$')
plt.plot(lambdas, delta_bits, marker='o', label=r'$\delta$')
plt.plot(lambdas, xi_bits, marker='o', label=r'$\xi$')

plt.title("Effect of λ on key sizes (selected keys)")
plt.xlabel("Security parameter λ (bits)")
plt.ylabel("Key size (bits)")
plt.grid(True)
plt.legend()
plt.tight_layout()
plt.show()
