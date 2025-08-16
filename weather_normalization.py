import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.preprocessing import MinMaxScaler, StandardScaler

# Load dataset
df = pd.read_csv("weather_data.csv")  # make sure this file exists

# Check if 'Temperature' column exists
if 'Temperature' not in df.columns:
    raise ValueError("The dataset must contain a 'Temperature' column.")

print("Original Dataset:\n", df.head())

# --- Apply Min-Max Normalization ---
minmax_scaler = MinMaxScaler()
df['MinMax_Temperature'] = minmax_scaler.fit_transform(df[['Temperature']])

# --- Apply Z-score Standardization ---
zscore_scaler = StandardScaler()
df['Zscore_Temperature'] = zscore_scaler.fit_transform(df[['Temperature']])

print("\nProcessed Dataset:\n", df.head())

plt.figure(figsize=(10, 5))
# Plot original temperature
plt.plot(df['Date'], df['Temperature'], label='Original Temperature', marker='o')

# Plot normalized temperature
plt.plot(df['Date'], df['Normalized_Temperature'], label=f'Normalized Temperature ({method})', marker='s')

plt.xlabel('Date')
plt.ylabel('Temperature')
plt.title(f'Original vs {method}')
plt.xticks(rotation=45)   # Rotate dates for readability
plt.legend()
plt.grid(True)

plt.savefig("plot.png")
plt.show()

# Save processed data
df.to_csv("processed_weather_data.csv", index=False)
print("\nProcessed data saved as 'processed_weather_data.csv'.")
