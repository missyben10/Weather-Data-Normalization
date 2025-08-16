# Weather Data Normalization 

[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/missyben10/Weather-Data-Normalization/blob/main/weather_normalization.py)

This project demonstrates how to **normalize weather temperature data** using two common methods:  
- **Min-Max Normalization** (scales values between 0 and 1)  
- **Z-score Standardization** (scales values relative to mean and standard deviation)  

The results are visualized and exported for further use in data science or machine learning tasks.  

---

## 🔹 Features
- Load temperature dataset from CSV (`weather_data.csv`)  
- Normalize data using:
  - Min-Max Normalization  
  - Z-score Standardization  
- Compare original and normalized values using line plots  
- Save processed dataset into `processed_weather_data.csv`  
- Save comparison graph as `plot.png`  

---

## 🔹 Installation
Clone this repository and install the required dependencies:

```bash
git clone https://github.com/missyben10/Weather-Data-Normalization.git
cd Weather-Data-Normalization
pip install -r requirements.txt
