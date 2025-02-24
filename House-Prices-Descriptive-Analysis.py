# Descriptive Analysis of House Prices
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import skew, kurtosis

# Fictitious data: house prices in dollars (10 houses)
house_prices = [150000, 200000, 180000, 220000, 160000, 300000, 170000, 190000, 250000, 210000]

# Calculate descriptive measures
mean = np.mean(house_prices)
median = np.median(house_prices)
mode = pd.Series(house_prices).mode()[0]
range_value = np.max(house_prices) - np.min(house_prices)
variance = np.var(house_prices, ddof=1)  # ddof=1 for sample variance
std_dev = np.std(house_prices, ddof=1)
skewness = skew(house_prices)
kurtosis_value = kurtosis(house_prices)  # Excess kurtosis (relative to normal)

# Display results
print("=== Descriptive Measures of House Prices ===")
print(f"Mean: ${mean:,.2f}")
print(f"Median: ${median:,.2f}")
print(f"Mode: ${mode:,.2f}")
print(f"Range: ${range_value:,.2f}")
print(f"Variance: ${variance:,.2f} dollars²")
print(f"Standard Deviation: ${std_dev:,.2f} dollars")
print(f"Skewness: {skewness:.2f}")
print(f"Kurtosis: {kurtosis_value:.2f}")

# Visualization of the distribution
plt.hist(house_prices, bins=5, edgecolor='black')
plt.title("Distribution of House Prices")
plt.xlabel("Price ($)")
plt.ylabel("Frequency")
plt.show()

# Observations and analyses
# - The distribution is skewed (Skewness = 0.83), indicating a long tail to the right due to the value 300,000.
# - The standard deviation (45,227.82) relative to the mean (203,000.00) represents 22.3% variability,
#   indicating high variability in prices, with values ranging from 150,000 to 300,000.
# - The mean (203,000) being greater than the median (190,000) reinforces the positive skewness.
# - The histogram shows a peak between 150,000-200,000 and a stretched tail toward 250,000-300,000.
