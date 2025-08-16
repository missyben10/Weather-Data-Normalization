import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.preprocessing import MinMaxScaler, StandardScaler

# Load temperature data from a CSV file
file_path = "weather_data.csv"  # Change this to your actual CSV file path
df = pd.read_csv(file_path)

# Check if 'Temperature' column exists
if 'Temperature' not in df.columns:
    raise ValueError("The dataset must contain a 'Temperature' column.")

# Display original dataset
print("Original Dataset:\n", df.head())

# Ask user for the normalization method
print("\nChoose a normalization method:")
print("1. Min-Max Normalization")
print("2. Z-score Standardization")
choice = input("Enter 1 or 2: ")

# Perform the chosen normalization
if choice == "1":
    scaler = MinMaxScaler()
    df['Normalized_Temperature'] = scaler.fit_transform(df[['Temperature']])
    method = "Min-Max Normalization"
elif choice == "2":
    scaler = StandardScaler()
    df['Normalized_Temperature'] = scaler.fit_transform(df[['Temperature']])
    method = "Z-score Standardization"
else:
    raise ValueError("Invalid choice. Please enter 1 or 2.")

# Display processed dataset
print("\nProcessed Dataset:\n", df.head())

# Visualize original vs. normalized data
plt.figure(figsize=(10, 5))
plt.plot(df['Temperature'], label='Original Temperature', marker='o')
plt.plot(df['Normalized_Temperature'], label=f'Normalized Temperature ({method})', marker='s')
plt.xlabel('Index')
plt.ylabel('Temperature')
plt.title(f'Original vs. {method}')
plt.legend()
plt.grid(True)

# Save and show the plot
plt.savefig("plot.png")
plt.show()

# Save the processed dataset
df.to_csv("processed_weather_data.csv", index=False)
print("\nProcessed data saved as 'processed_weather_data.csv'.")
