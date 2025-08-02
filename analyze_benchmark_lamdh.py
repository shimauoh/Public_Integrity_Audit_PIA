import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# === Define data for λ=128 ===
tag_128 = [
    {"Block size":256, "Basic":0.064, "Enhanced":0.1194, "Algebraic":0.7323},
    {"Block size":512, "Basic":0.0903, "Enhanced":0.1894, "Algebraic":1.4625},
    {"Block size":1024,"Basic":0.1787, "Enhanced":0.4042, "Algebraic":2.7993},
    {"Block size":2048,"Basic":0.2396, "Enhanced":0.7863, "Algebraic":5.3375},
    {"Block size":4096,"Basic":0.3484, "Enhanced":0.8392, "Algebraic":13.4866},
    {"Block size":5120,"Basic":1.2090, "Enhanced":1.9875, "Algebraic":16.9548},
]
csp_128 = [
    {"Block size":256, "Basic":0.0521, "Enhanced":0.0677, "Algebraic":0.2429},
    {"Block size":512, "Basic":0.101,  "Enhanced":0.1134, "Algebraic":0.5018},
    {"Block size":1024,"Basic":0.1669, "Enhanced":0.1764, "Algebraic":1.3196},
    {"Block size":2048,"Basic":0.1394, "Enhanced":0.2196, "Algebraic":3.9144},
    {"Block size":4096,"Basic":0.2800, "Enhanced":0.4500, "Algebraic":7.0000},
    {"Block size":5120,"Basic":0.3100, "Enhanced":0.5000, "Algebraic":8.0000},
]
tpa_128 = [
    {"Block size":256, "Basic":0.022,  "Enhanced":0.0311, "Algebraic":0.2928},
    {"Block size":512, "Basic":0.0315, "Enhanced":0.03,   "Algebraic":0.5444},
    {"Block size":1024,"Basic":0.0337, "Enhanced":0.0212, "Algebraic":1.3242},
    {"Block size":2048,"Basic":0.0125, "Enhanced":0.0179, "Algebraic":3.4402},
    {"Block size":4096,"Basic":0.0200, "Enhanced":0.0250, "Algebraic":6.0000},
    {"Block size":5120,"Basic":0.0250, "Enhanced":0.0300, "Algebraic":7.5000},
]

# === Repeat similarly: data for λ=192 and λ=256 ===
# For λ=192
tag_192 = [
    {"Block size":256, "Basic":0.0606, "Enhanced":0.1322, "Algebraic":0.8436},
    {"Block size":512, "Basic":0.1585, "Enhanced":0.2644, "Algebraic":2.1087},
    {"Block size":1024,"Basic":0.1221, "Enhanced":0.3582, "Algebraic":4.6367},
    {"Block size":2048,"Basic":0.2031, "Enhanced":0.6289, "Algebraic":6.4946},
    {"Block size":4096,"Basic":0.3180, "Enhanced":0.9389, "Algebraic":12.7908},
    {"Block size":5120,"Basic":0.5820, "Enhanced":1.8281, "Algebraic":16.1915},
]
csp_192 = [
    {"Block size":256, "Basic":0.058,  "Enhanced":0.0799, "Algebraic":0.7618},
    {"Block size":512, "Basic":0.9922, "Enhanced":0.1516, "Algebraic":1.8151},
    {"Block size":1024,"Basic":0.1064, "Enhanced":0.3038, "Algebraic":1.9906},
    {"Block size":2048,"Basic":0.1404, "Enhanced":0.2395, "Algebraic":4.7389},
    {"Block size":4096,"Basic":0.2910, "Enhanced":0.3935, "Algebraic":9.3073},
    {"Block size":5120,"Basic":0.3946, "Enhanced":0.4642, "Algebraic":11.7606},
]
tpa_192 = [
    {"Block size":256, "Basic":0.0145, "Enhanced":0.055,  "Algebraic":0.5444},
    {"Block size":512, "Basic":0.0215, "Enhanced":0.0513, "Algebraic":1.2903},
    {"Block size":1024,"Basic":0.0294, "Enhanced":0.0216, "Algebraic":2.061},
    {"Block size":2048,"Basic":0.0101, "Enhanced":0.0154, "Algebraic":4.2524},
    {"Block size":4096,"Basic":0.0098, "Enhanced":0.0151, "Algebraic":8.9080},
    {"Block size":5120,"Basic":0.0423, "Enhanced":0.0160, "Algebraic":11.2630}
]
# For λ=256
tag_256 = [
    {"Block size":256, "Basic":0.0788, "Enhanced":0.1428, "Algebraic":1.0106},
    {"Block size":512, "Basic":0.165,  "Enhanced":0.3575, "Algebraic":2.1524},
    {"Block size":1024,"Basic":0.1432, "Enhanced":0.3641, "Algebraic":3.857},
    {"Block size":2048,"Basic":0.195,  "Enhanced":0.6453, "Algebraic":7.347},
    {"Block size":4096,"Basic":0.4110, "Enhanced":1.7385, "Algebraic":15.7814},
    {"Block size":5120,"Basic":0.7665, "Enhanced":2.8250, "Algebraic":26.4262},
]
csp_256 = [
    {"Block size":256, "Basic":0.0592, "Enhanced":0.0687, "Algebraic":0.6274},
    {"Block size":512, "Basic":0.2056, "Enhanced":0.344,  "Algebraic":1.9454},
    {"Block size":1024,"Basic":0.1004, "Enhanced":0.2975, "Algebraic":2.2427},
    {"Block size":2048,"Basic":0.1334, "Enhanced":0.2494, "Algebraic":6.0633},
    {"Block size":4096,"Basic":0.3893, "Enhanced":0.4977, "Algebraic":18.8334},
    {"Block size":5120,"Basic":0.4842, "Enhanced":0.6067, "Algebraic":18.4530},
]
tpa_256 = [
    {"Block size":256, "Basic":0.0366, "Enhanced":0.038,  "Algebraic":0.5802},
    {"Block size":512, "Basic":0.0486, "Enhanced":0.0488, "Algebraic":1.1618},
    {"Block size":1024,"Basic":0.0296, "Enhanced":0.0198,  "Algebraic":2.2458},
    {"Block size":2048,"Basic":0.0148, "Enhanced":0.0152, "Algebraic":5.3725},
    {"Block size":4096,"Basic":0.0430, "Enhanced":0.0161, "Algebraic":9.5602},
    {"Block size":5120,"Basic":0.0108, "Enhanced":0.0414, "Algebraic":20.2298}
]
# For brevity, I’ll keep using your own real data; you can extend/add more

# === Create DataFrames ===
df_tag_128 = pd.DataFrame(tag_128)
df_tag_192 = pd.DataFrame(tag_192)
df_tag_256 = pd.DataFrame(tag_256)

df_csp_128 = pd.DataFrame(csp_128)
df_csp_192 = pd.DataFrame(csp_192)
df_csp_256 = pd.DataFrame(csp_256)

df_tpa_128 = pd.DataFrame(tpa_128)
df_tpa_192 = pd.DataFrame(tpa_192)
df_tpa_256= pd.DataFrame(tpa_256)

def plot_three_lambdas(metric_name, dfs, ylabel,ylim=None, yticks=None):
    """
    metric_name: e.g., "Tag generation time vs Block size"
    dfs: list of three dfs for λ=128,192,256
    ylabel: label for y axis
    """
    fig, axes = plt.subplots(1, 3, figsize=(18, 5), sharey=True)
    lambdas = [128, 192, 256]
    
    for ax, df, lam in zip(axes, dfs, lambdas):
        ax.plot(df["Block size"], df["Basic"], marker='o', label="Basic Schnorr")
        ax.plot(df["Block size"], df["Enhanced"], marker='o', label="Enhanced Schnorr")
        ax.plot(df["Block size"], df["Algebraic"], marker='o', label="Algebraic Signature")
        ax.set_title(f"{metric_name} (λ={lam})")
        ax.set_xlabel("Block size (bytes)")
        ax.grid(True)
        
    if ylim:
     ax.set_ylim(ylim)
     ax.set_yticks(np.arange(ylim[0], ylim[1] + 1, 1))  # 1 ms steps

    axes[0].set_ylabel(ylabel)
    axes[2].legend(title="Algorithm", loc='upper left')
    plt.tight_layout()
    plt.show()

# === Plot: tag generation time vs block size for λ=128,192,256 ===
plot_three_lambdas("Tag generation time vs Block size",
                   [df_tag_128, df_tag_192, df_tag_256],
                   "Avg tag gen time (ms)")

# === Plot: CSP proof gen time vs block size ===
plot_three_lambdas("CSP proof generation time vs Block size",
                   [df_csp_128, df_csp_192, df_csp_256],
                   "CSP proof gen time (ms)")

# === Plot: TPA verification time vs block size ===
plot_three_lambdas("TPA verification time vs Block size",
                   [df_tpa_128, df_tpa_192, df_tpa_256],
                   "TPA verification time (ms)")
