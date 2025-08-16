import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.preprocessing import MinMaxScaler, StandardScaler

# Load dataset
df = pd.read_csv("weather_data.csv")  # Make sure this file exists in Colab or project folder

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

# Original
plt.plot(df['Date'], df['Temperature'], label='Original Temperature', marker='o')

# Min-Max
plt.plot(df['Date'], df['MinMax_Temperature'], label='Min-Max Normalization', marker='s')

# Z-score
plt.plot(df['Date'], df['Zscore_Temperature'], label='Z-score Standardization', marker='^')

# Labels & title
plt.xlabel('Date')
plt.ylabel('Temperature')
plt.title('Original vs Min-Max vs Z-score')
plt.xticks(rotation=45)  # Rotate dates for readability
plt.legend()
plt.grid(True)

# Save and show plot
plt.savefig("plot.png")
plt.show()

# Save processed dataset
df.to_csv("processed_weather_data.csv", index=False)
print("\nProcessed data saved as 'processed_weather_data.csv'.")
