# House-Prices-Descriptive-Analysis
Descriptive statistical analysis of fictitious house prices, including measures like mean, median, and skewness, with visualization

# House Prices Descriptive Analysis

This project performs a descriptive statistical analysis of fictitious house prices using Python. It calculates key metrics such as mean, median, mode, range, variance, standard deviation, skewness, and kurtosis to explore the distribution and variability of house prices. The analysis includes a histogram visualization to illustrate the data distribution.

## Features
- Computes basic statistical measures (mean, median, mode, range, variance, standard deviation).
- Evaluates the shape of the distribution using skewness and kurtosis.
- Generates a histogram to visually represent the distribution of house prices.

## Data
The dataset used is a small, fictitious list of 10 house prices in dollars, ranging from $150,000 to $300,000. This serves as a simplified example but can be expanded with real datasets (e.g., from Kaggle).

## Observations
- The distribution is positively skewed (Skewness = 0.83), with a long tail to the right due to the outlier value of $300,000.
- The standard deviation ($45,227.82) relative to the mean ($203,000.00) indicates 22.3% variability, suggesting high variability in prices.
- The histogram shows a peak between $150,000 and $200,000, with a stretched tail toward $250,000–$300,000.

## Requirements
- Python 3.x
- Libraries: numpy, pandas, matplotlib, scipy

## How to Run
1. Clone this repository.
2. Install the required libraries using `pip install numpy pandas matplotlib scipy`.
3. Run the script (`python house_prices_analysis.py`) to see the results and visualization.

## Future Improvements
- Expand the analysis with a real dataset (e.g., Kaggle "House Prices" dataset) for more robust insights.
- Add more advanced visualizations or statistical tests.

## License
MIT License
