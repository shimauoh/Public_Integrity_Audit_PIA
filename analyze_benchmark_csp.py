import pandas as pd
import matplotlib.pyplot as plt

# === Data for CSP proof gen time ===
# For λ=128
csp_128 = [
    {"Block size":256, "Basic":0.0521, "Enhanced":0.0677, "Algebraic":0.2429},
    {"Block size":512, "Basic":0.101,  "Enhanced":0.1134, "Algebraic":0.5018},
    {"Block size":1024,"Basic":0.1669, "Enhanced":0.1764, "Algebraic":1.3196},
    {"Block size":2048,"Basic":0.1394, "Enhanced":0.2196, "Algebraic":3.9144},
    {"Block size":4096,"Basic":0.5206, "Enhanced":0.3141, "Algebraic":8.6143},
    {"Block size":5120,"Basic":0.2928, "Enhanced":0.5066, "Algebraic":11.5727},
]

# For λ=192
csp_192 = [
    {"Block size":256, "Basic":0.058,  "Enhanced":0.0799, "Algebraic":0.7618},
    {"Block size":512, "Basic":0.9922, "Enhanced":0.1516, "Algebraic":1.8151},
    {"Block size":1024,"Basic":0.1064, "Enhanced":0.3038, "Algebraic":1.9906},
    {"Block size":2048,"Basic":0.1404, "Enhanced":0.2395, "Algebraic":4.7389},
    {"Block size":4096,"Basic":0.3946, "Enhanced":0.3935, "Algebraic":9.3073},
    {"Block size":5120,"Basic":0.2910, "Enhanced":0.4642, "Algebraic":11.7606},
]

# For λ=256
csp_256 = [
    {"Block size":256, "Basic":0.0592, "Enhanced":0.0687, "Algebraic":0.6274},
    {"Block size":512, "Basic":0.2056, "Enhanced":0.344,  "Algebraic":1.9454},
    {"Block size":1024,"Basic":0.1004, "Enhanced":0.2975, "Algebraic":2.2427},
    {"Block size":2048,"Basic":0.1334, "Enhanced":0.2494, "Algebraic":6.0633},
    {"Block size":4096,"Basic":0.3893, "Enhanced":0.4977, "Algebraic":18.8334},
    {"Block size":5120,"Basic":0.4842, "Enhanced":0.6067, "Algebraic":18.4530},
]

# === Create DataFrames ===
df_csp_128 = pd.DataFrame(csp_128)
df_csp_192 = pd.DataFrame(csp_192)
df_csp_256 = pd.DataFrame(csp_256)

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

# === Plot separately for each λ ===
plot_csp_vs_block(df_csp_128, 128)
plot_csp_vs_block(df_csp_192, 192)
plot_csp_vs_block(df_csp_256, 256)
