import pandas as pd
import matplotlib.pyplot as plt

# === CSP proof gen time data ===
csp_128 = [
    {"Block size":256, "Basic":0.0521, "Enhanced":0.0677, "Algebraic":0.2429},
    {"Block size":512, "Basic":0.101,  "Enhanced":0.1134, "Algebraic":0.5018},
    {"Block size":1024,"Basic":0.1669, "Enhanced":0.1764, "Algebraic":1.3196},
    {"Block size":2048,"Basic":0.1394, "Enhanced":0.2196, "Algebraic":3.9144},
]

csp_192 = [
    {"Block size":256, "Basic":0.058,  "Enhanced":0.0799, "Algebraic":0.7618},
    {"Block size":512, "Basic":0.9922, "Enhanced":0.1516, "Algebraic":1.8151},
    {"Block size":1024,"Basic":0.1064, "Enhanced":0.3038, "Algebraic":1.9906},
    {"Block size":2048,"Basic":0.1404, "Enhanced":0.2395, "Algebraic":4.7389},
]

csp_256 = [
    {"Block size":256, "Basic":0.0592, "Enhanced":0.0687, "Algebraic":0.6274},
    {"Block size":512, "Basic":0.2056, "Enhanced":0.344,  "Algebraic":1.9454},
    {"Block size":1024,"Basic":0.1004, "Enhanced":0.2975, "Algebraic":2.2427},
    {"Block size":2048,"Basic":0.1334, "Enhanced":0.2494, "Algebraic":6.0633},
]

# === TPA verification time data ===
tpa_128 = [
    {"Block size":256, "Basic":0.022,  "Enhanced":0.0311, "Algebraic":0.2928},
    {"Block size":512, "Basic":0.0315, "Enhanced":0.03,   "Algebraic":0.5444},
    {"Block size":1024,"Basic":0.0337, "Enhanced":0.0212, "Algebraic":1.3242},
    {"Block size":2048,"Basic":0.0125, "Enhanced":0.0179, "Algebraic":3.4402},
    {"Block size":4096,"Basic":0.0101, "Enhanced":0.0233, "Algebraic":8.3534},
    {"Block size":5120,"Basic":0.0229, "Enhanced":0.0127, "Algebraic":11.5859},
]

tpa_192 = [
    {"Block size":256, "Basic":0.0145, "Enhanced":0.055,  "Algebraic":0.5444},
    {"Block size":512, "Basic":0.0215, "Enhanced":0.0513, "Algebraic":1.2903},
    {"Block size":1024,"Basic":0.0294, "Enhanced":0.0216, "Algebraic":2.061},
    {"Block size":2048,"Basic":0.0101, "Enhanced":0.0154, "Algebraic":4.2524},
    {"Block size":4096,"Basic":0.0098, "Enhanced":0.0151, "Algebraic":8.9080},
    {"Block size":5120,"Basic":0.0423, "Enhanced":0.0130, "Algebraic":11.2630}
]

tpa_256 = [
    {"Block size":256, "Basic":0.0366, "Enhanced":0.038,  "Algebraic":0.5802},
    {"Block size":512, "Basic":0.0486, "Enhanced":0.0388, "Algebraic":1.1618},
    {"Block size":1024,"Basic":0.0296, "Enhanced":0.019,  "Algebraic":2.2458},
    {"Block size":2048,"Basic":0.0148, "Enhanced":0.0152, "Algebraic":5.3725},
    {"Block size":4096,"Basic":0.0430, "Enhanced":0.0161, "Algebraic":9.5602},
    {"Block size":5120,"Basic":0.0108, "Enhanced":0.0414, "Algebraic":20.2298}
]

# === Convert to DataFrames ===
df_csp_128 = pd.DataFrame(csp_128); df_tpa_128 = pd.DataFrame(tpa_128)
df_csp_192 = pd.DataFrame(csp_192); df_tpa_192 = pd.DataFrame(tpa_192)
df_csp_256 = pd.DataFrame(csp_256); df_tpa_256 = pd.DataFrame(tpa_256)

# === Plot function with subplots ===
def plot_csp_tpa(df_csp, df_tpa, λ):
    fig, axes = plt.subplots(1,2, figsize=(12,5))
    
    # Left: CSP proof gen time
    axes[0].plot(df_csp["Block size"], df_csp["Basic"], marker='o', label="Basic Schnorr")
    axes[0].plot(df_csp["Block size"], df_csp["Enhanced"], marker='o', label="Enhanced Schnorr")
    axes[0].plot(df_csp["Block size"], df_csp["Algebraic"], marker='o', label="Algebraic Signature")
    axes[0].set_title(f"CSP Proof Gen Time vs Block Size (λ={λ})")
    axes[0].set_xlabel("Block size (bytes)")
    axes[0].set_ylabel("Time (ms)")
    axes[0].grid(True)
    
    # Right: TPA verification time
    axes[1].plot(df_tpa["Block size"], df_tpa["Basic"], marker='o', label="Basic Schnorr")
    axes[1].plot(df_tpa["Block size"], df_tpa["Enhanced"], marker='o', label="Enhanced Schnorr")
    axes[1].plot(df_tpa["Block size"], df_tpa["Algebraic"], marker='o', label="Algebraic Signature")
    axes[1].set_title(f"TPA Verification Time vs Block Size (λ={λ})")
    axes[1].set_xlabel("Block size (bytes)")
    axes[1].set_ylabel("Time (ms)")
    axes[1].grid(True)
    
    # Add legend (shared)
    axes[1].legend(title="Algorithm", loc='upper left')
    plt.tight_layout()
    plt.show()

# === Call for each λ ===
plot_csp_tpa(df_csp_128, df_tpa_128, 128)
plot_csp_tpa(df_csp_192, df_tpa_192, 192)
plot_csp_tpa(df_csp_256, df_tpa_256, 256)
