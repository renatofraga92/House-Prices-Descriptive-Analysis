import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import skew, kurtosis

house_prices = [150000, 200000, 180000, 220000, 160000, 300000, 170000, 190000, 250000, 210000]

mean = np.mean(house_prices)
median = np.median(house_prices)
mode = pd.Series(house_prices).mode()[0]
range_value = np.max(house_prices) - np.min(house_prices)
variance = np.var(house_prices, ddof=1)
std_dev = np.std(house_prices, ddof=1)
skewness = skew(house_prices)
kurtosis_value = kurtosis(house_prices)

print("=== Descriptive Measures of House Prices ===")
print(f"Mean: ${mean:,.2f}")
print(f"Median: ${median:,.2f}")
print(f"Mode: ${mode:,.2f}")
print(f"Range: ${range_value:,.2f}")
print(f"Variance: ${variance:,.2f} dollars²")
print(f"Standard Deviation: ${std_dev:,.2f} dollars")
print(f"Skewness: {skewness:.2f}")
print(f"Kurtosis: {kurtosis_value:.2f}")

plt.hist(house_prices, bins=5, edgecolor='black')
plt.title("Distribution of House Prices")
plt.xlabel("Price ($)")
plt.ylabel("Frequency")
plt.show()
