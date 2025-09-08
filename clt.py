import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import norm

def load_data(path="dataset1.csv", col="bat_landing_to_food"):
    df = pd.read_csv(path)
    return pd.to_numeric(df[col], errors="coerce").dropna().astype(float).values

def demonstrate_clt(data):
    # Calculate sample means for CLT(sample is around 1000 and large )
    sample_means = []
    for _ in range(50000):
        sample = np.random.choice(data, size=100, replace=True)
        sample_means.append(sample.mean())
    sample_means = np.array(sample_means)

    # Plot CLT histogram 
    plt.hist(sample_means, bins=40, density=True, alpha=0.7, label='Sample Means (CLT)')
    plt.title('CLT: Distribution of Sample Means')
    plt.xlabel('Sample Mean')
    plt.ylabel('Density')
    plt.legend()
    plt.show()


if __name__ == "__main__":
    data = load_data("dataset1.csv")
    n = len(data)
    mean = data.mean()
    std = data.std(ddof=1)

    print(f"n = {n}, sample mean = {mean:.4f}, sd = {std:.4f}")
    demonstrate_clt(data)
  