import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.preprocessing import MinMaxScaler, StandardScaler

# Load dataset
df = pd.read_csv("weather_data.csv")  # make sure this file is in the repo

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

# --- Visualization ---
plt.figure(figsize=(12,6))
plt.plot(df['Temperature'], label='Original Temperature', marker='o')
plt.plot(df['MinMax_Temperature'], label='Min-Max Normalization', marker='s')
plt.plot(df['Zscore_Temperature'], label='Z-score Standardization', marker='^')
plt.xlabel('Index')
plt.ylabel('Temperature')
plt.title('Original vs Min-Max vs Z-score')
plt.legend()
plt.grid(True)

# Save the plot as an image
plt.savefig("plot.png")
plt.show()

# Save processed data
df.to_csv("processed_weather_data.csv", index=False)
print("\nProcessed data saved as 'processed_weather_data.csv'.")
