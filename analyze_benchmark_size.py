import matplotlib.pyplot as plt
import numpy as np

# Security parameters and tag sizes
security_params = ['128', '192', '256']
basic_schnorr = [32, 48, 64]
enhanced_schnorr = [32, 48, 64]
algebraic_signature = [24, 24, 32]

x = np.arange(len(security_params))  # the label locations
width = 0.25  # the width of the bars

fig, ax = plt.subplots(figsize=(8,6))

# Plot bars
bars1 = ax.bar(x - width, basic_schnorr, width, label='Basic Schnorr')
bars2 = ax.bar(x, enhanced_schnorr, width, label='Enhanced Schnorr')
bars3 = ax.bar(x + width, algebraic_signature, width, label='Algebraic Signature')

# Labels and title
ax.set_xlabel('Security Parameter ($\\lambda$)', fontsize=12)
ax.set_ylabel('Tag Size (Bytes)', fontsize=12)
ax.set_title('Tag Size Comparison for Different Security Parameters', fontsize=14)
ax.set_xticks(x)
ax.set_xticklabels(security_params)
ax.legend()

# Show values on bars (optional)
for bars in [bars1, bars2, bars3]:
    for bar in bars:
        height = bar.get_height()
        ax.annotate(f'{height}',
                    xy=(bar.get_x() + bar.get_width() / 2, height),
                    xytext=(0, 3),  # 3 points vertical offset
                    textcoords="offset points",
                    ha='center', va='bottom', fontsize=10)

plt.tight_layout()
plt.show()
