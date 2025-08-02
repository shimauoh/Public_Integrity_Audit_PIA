import pandas as pd
import matplotlib.pyplot as plt

# === Define data ===
# For λ=128
data_128 = [
    {"Block size":256, "Basic":0.064, "Enhanced":0.1194, "Algebraic":0.7323},
    {"Block size":512, "Basic":0.0903, "Enhanced":0.1894, "Algebraic":1.4625},
    {"Block size":1024,"Basic":0.1787, "Enhanced":0.4042, "Algebraic":2.7993},
    {"Block size":2048,"Basic":0.2396, "Enhanced":0.7863, "Algebraic":5.3375},
    {"Block size":4096,"Basic":0.3484, "Enhanced":0.8392, "Algebraic":13.4866},
    {"Block size":5120,"Basic":1.9875, "Enhanced":2.8250, "Algebraic":16.9548},
    
]

# For λ=192
data_192 = [
    {"Block size":256, "Basic":0.0606, "Enhanced":0.1322, "Algebraic":0.8436},
    {"Block size":512, "Basic":0.1585, "Enhanced":0.2644, "Algebraic":2.1087},
    {"Block size":1024,"Basic":0.1221, "Enhanced":0.3582, "Algebraic":4.6367},
    {"Block size":2048,"Basic":0.2031, "Enhanced":0.6289, "Algebraic":6.4946},
    {"Block size":4096,"Basic":0.3180, "Enhanced":1.2090, "Algebraic":12.7908},
    {"Block size":5120,"Basic":0.5820, "Enhanced":0.9389, "Algebraic":16.1915},
]

# For λ=256
data_256 = [
    {"Block size":256, "Basic":0.0788, "Enhanced":0.1428, "Algebraic":1.0106},
    {"Block size":512, "Basic":0.165,  "Enhanced":0.3575, "Algebraic":2.1524},
    {"Block size":1024,"Basic":0.1432, "Enhanced":0.3641, "Algebraic":3.857},
    {"Block size":2048,"Basic":0.195,  "Enhanced":0.6453, "Algebraic":7.347},
    {"Block size":4096,"Basic":0.4110, "Enhanced":1.5738, "Algebraic":15.7814},
    {"Block size":5120,"Basic":0.7665, "Enhanced":1.1828, "Algebraic":26.4262},
]

# === Create DataFrames ===
df128 = pd.DataFrame(data_128)
df192 = pd.DataFrame(data_192)
df256 = pd.DataFrame(data_256)

# === Define plotting function ===
def plot_tag_time_vs_block(df, λ):
    plt.figure(figsize=(8,5))
    plt.plot(df["Block size"], df["Basic"],   marker='o', label="Basic Schnorr")
    plt.plot(df["Block size"], df["Enhanced"],marker='o', label="Enhanced Schnorr")
    plt.plot(df["Block size"], df["Algebraic"],marker='o', label="Algebraic Signature")
    plt.title(f"Avg tag generation time vs Block size (λ={λ})")
    plt.xlabel("Block size (bytes)")
    plt.ylabel("Avg time per block (ms)")
    plt.grid(True)
    plt.legend()
    plt.tight_layout()
    plt.show()
    

# === Plot separately for each λ ===
plot_tag_time_vs_block(df128, 128)
plot_tag_time_vs_block(df192, 192)
plot_tag_time_vs_block(df256, 256)




# === Define plotting function ===
def plot_csp_vs_block(df, λ):
    plt.figure(figsize=(8,5))
    plt.plot(df["Block size"], df["Basic"],   marker='o', label="Basic Schnorr")
    plt.plot(df["Block size"], df["Enhanced"],marker='o', label="Enhanced Schnorr")
    plt.plot(df["Block size"], df["Algebraic"],marker='o', label="Algebraic Signature")
    plt.title(f"CSP Proof generation time vs Block size (λ={λ})")
    plt.xlabel("Block size (bytes)")
    plt.ylabel("CSP proof gen time (ms)")
    plt.grid(True)
    plt.legend()
    plt.tight_layout()
    plt.show()

