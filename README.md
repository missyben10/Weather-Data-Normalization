# Weather Data Normalization 

This project normalizes weather temperature data using **Min-Max Normalization** and **Z-score Standardization**.  
It also visualizes the original vs normalized data and saves the processed dataset.

---

## 🔹 Features
- Reads weather data from CSV (`weather_data.csv`)
- Applies **Min-Max Normalization** (scales 0–1)
- Applies **Z-score Standardization** (mean=0, std=1)
- Creates line plot comparison
- Saves processed dataset to `processed_weather_data.csv`
- Saves plot as `plot.png`

---

## 🔹 Installation
Clone the repository and install requirements:
```bash
git clone https://github.com/missyben10/Weather-Data-Normalization.git
cd Weather-Data-Normalization
pip install -r requirements.txt
