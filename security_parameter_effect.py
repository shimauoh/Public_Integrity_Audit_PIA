import pandas as pd
import matplotlib.pyplot as plt

# === Manually define data ===
# Data for λ=128
data_128 = [
    {"Metric":"Key generation time (ms)", "Block size":256, "Basic":247.43, "Enhanced":247.43, "Algebraic":3.58},
    {"Metric":"Avg time per block (ms)", "Block size":256, "Basic":0.064, "Enhanced":0.1194, "Algebraic":0.7323},
    {"Metric":"CSP proof gen time (ms)", "Block size":256, "Basic":0.0521, "Enhanced":0.0677, "Algebraic":0.2429},
    {"Metric":"TPA verification time (ms)", "Block size":256, "Basic":0.022, "Enhanced":0.0311, "Algebraic":0.2928},
    {"Metric":"tag size (bytes)", "Block size":256, "Basic":35, "Enhanced":35, "Algebraic":16},
]

# Data for λ=192
data_192 = [
    {"Metric":"Key generation time (ms)", "Block size":256, "Basic":271.79, "Enhanced":271.79, "Algebraic":3.09},
    {"Metric":"Avg time per block (ms)", "Block size":256, "Basic":0.0606, "Enhanced":0.1322, "Algebraic":0.8436},
    {"Metric":"CSP proof gen time (ms)", "Block size":256, "Basic":0.058, "Enhanced":0.0799, "Algebraic":0.7618},
    {"Metric":"TPA verification time (ms)", "Block size":256, "Basic":0.0145, "Enhanced":0.055, "Algebraic":0.5444},
    {"Metric":"tag size (bytes)", "Block size":256, "Basic":48, "Enhanced":48, "Algebraic":24},
]

# Data for λ=256
data_256 = [
    {"Metric":"Key generation time (ms)", "Block size":256, "Basic":171.43, "Enhanced":171.43, "Algebraic":4.34},
    {"Metric":"Avg time per block (ms)", "Block size":256, "Basic":0.0788, "Enhanced":0.1428, "Algebraic":1.0106},
    {"Metric":"CSP proof gen time (ms)", "Block size":256, "Basic":0.0592, "Enhanced":0.0687, "Algebraic":0.6274},
    {"Metric":"TPA verification time (ms)", "Block size":256, "Basic":0.0366, "Enhanced":0.038, "Algebraic":0.5802},
    {"Metric":"tag size (bytes)", "Block size":256, "Basic":64, "Enhanced":64, "Algebraic":32},
]

# === Create DataFrames ===
df128 = pd.DataFrame(data_128)
df192 = pd.DataFrame(data_192)
df256 = pd.DataFrame(data_256)

# === Plot: Effect of security parameter on key generation time ===
keygen_times = pd.DataFrame({
    'λ': [128,192,256],
    'Basic': [247.43, 271.79, 171.43],
    'Enhanced': [247.43, 271.79, 171.43],
    'Algebraic': [3.58, 3.09, 4.34]
})
plt.figure(figsize=(8,5))
plt.plot(keygen_times['λ'], keygen_times['Basic'], marker='o', label="Basic Schnorr")
plt.plot(keygen_times['λ'], keygen_times['Enhanced'], marker='o', label="Enhanced Schnorr")
plt.plot(keygen_times['λ'], keygen_times['Algebraic'], marker='o', label="Algebraic Signature")
plt.title("Effect of security parameter on key generation time")
plt.xlabel("Security parameter λ (bits)")
plt.ylabel("Key generation time (ms)")
plt.grid(True)
plt.legend()
plt.tight_layout()
plt.show()

# === Plot: Effect of security parameter on tag size ===
tag_sizes = pd.DataFrame({
    'λ': [128,192,256],
    'Basic': [35,48,64],
    'Enhanced': [35,48,64],
    'Algebraic': [16,24,32]
})
plt.figure(figsize=(8,5))
plt.plot(tag_sizes['λ'], tag_sizes['Basic'], marker='o', label="Basic Schnorr")
plt.plot(tag_sizes['λ'], tag_sizes['Enhanced'], marker='o', label="Enhanced Schnorr")
plt.plot(tag_sizes['λ'], tag_sizes['Algebraic'], marker='o', label="Algebraic Signature")
plt.title("Effect of security parameter on tag size")
plt.xlabel("Security parameter λ (bits)")
plt.ylabel("Tag size (bytes)")
plt.grid(True)
plt.legend()
plt.tight_layout()
plt.show()

# === Plot: Effect of security parameter on avg time per block ===
avg_times = pd.DataFrame({
    'λ': [128,192,256],
    'Basic': [0.064,0.0606,0.0788],
    'Enhanced': [0.1194,0.1322,0.1428],
    'Algebraic': [0.7323,0.8436,1.0106]
})
plt.figure(figsize=(8,5))
plt.plot(avg_times['λ'], avg_times['Basic'], marker='o', label="Basic Schnorr")
plt.plot(avg_times['λ'], avg_times['Enhanced'], marker='o', label="Enhanced Schnorr")
plt.plot(avg_times['λ'], avg_times['Algebraic'], marker='o', label="Algebraic Signature")
plt.title("Effect of security parameter on average tag generation time")
plt.xlabel("Security parameter λ (bits)")
plt.ylabel("Avg time per block (ms)")
plt.grid(True)
plt.legend()
plt.tight_layout()
plt.show()
avg_times = pd.DataFrame({
    'λ': [128, 192, 256],
    'Basic':    [0.064, 0.0606, 0.0788],
    'Enhanced': [0.1194, 0.1322, 0.1428],
    'Algebraic':[0.7323, 0.8436, 1.0106]
})

csp_times = pd.DataFrame({
    'λ': [128, 192, 256],
    'Basic':    [0.0521, 0.0580, 0.0592],
    'Enhanced': [0.0677, 0.0799, 0.0687],
    'Algebraic':[0.2429, 0.7618, 0.6274]
})

tpa_times = pd.DataFrame({
    'λ': [128, 192, 256],
    'Basic':    [0.0220, 0.0145, 0.0366],
    'Enhanced': [0.0311, 0.0550, 0.0380],
    'Algebraic':[0.2928, 0.5444, 0.5802]
})

# === Plot 1: Avg tag‑gen time per block vs λ ===
plt.figure(figsize=(8,5))
plt.plot(avg_times['λ'], avg_times['Basic'],    marker='o', label="Basic Schnorr")
plt.plot(avg_times['λ'], avg_times['Enhanced'], marker='o', label="Enhanced Schnorr")
plt.plot(avg_times['λ'], avg_times['Algebraic'],marker='o', label="Algebraic Signature")
plt.title("Effect of Security Parameter on Average Tag‑Generation Time")
plt.xlabel("Security parameter λ (bits)")
plt.ylabel("Avg tag‑gen time per block (ms)")
plt.grid(True)
plt.legend()
plt.tight_layout()
plt.show()

# === Plot 2: CSP proof‑generation time vs λ ===
plt.figure(figsize=(8,5))
plt.plot(csp_times['λ'], csp_times['Basic'],    marker='o', label="Basic Schnorr")
plt.plot(csp_times['λ'], csp_times['Enhanced'], marker='o', label="Enhanced Schnorr")
plt.plot(csp_times['λ'], csp_times['Algebraic'],marker='o', label="Algebraic Signature")
plt.title("Effect of Security Parameter on CSP Proof‑Generation Time")
plt.xlabel("Security parameter λ (bits)")
plt.ylabel("CSP proof‑generation time (ms)")
plt.grid(True)
plt.legend()
plt.tight_layout()
plt.show()

# === Plot 3: TPA verification time vs λ ===
plt.figure(figsize=(8,5))
plt.plot(tpa_times['λ'], tpa_times['Basic'],    marker='o', label="Basic Schnorr")
plt.plot(tpa_times['λ'], tpa_times['Enhanced'], marker='o', label="Enhanced Schnorr")
plt.plot(tpa_times['λ'], tpa_times['Algebraic'],marker='o', label="Algebraic Signature")
plt.title("Effect of Security Parameter on TPA Verification Time")
plt.xlabel("Security parameter λ (bits)")
plt.ylabel("TPA verification time (ms)")
plt.grid(True)
plt.legend()
plt.tight_layout()
plt.show()
