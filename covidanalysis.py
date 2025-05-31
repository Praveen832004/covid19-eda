import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# Load Data set

df = pd.read_csv("owid-covid-data.csv")
print(df.head())
print(df.shape)
print(df.columns)
df.head()
df.isnull().sum().sort_values(ascending=False)

#Remove colums with more tha 90% null value

threshold = len(df) * 0.9
df_clean = df.dropna(thresh=threshold, axis=1).copy()

#Fill null with 0
df_clean['new_cases'] = df_clean['new_cases'].fillna(0)
df_clean['new_deaths'] = df_clean['new_deaths'].fillna(0)
df_clean['date'] = pd.to_datetime(df_clean['date'])

# style for better visuals
sns.set(style="whitegrid")

#specific country for focused analysis
country = "India"  

#Filtering data for the country
country_data = df_clean[df_clean['location'] == country]

# Plot 1: New Cases Over Time
plt.figure(figsize=(12, 6))
plt.plot(country_data['date'], country_data['new_cases'], label='New Cases')
plt.title(f"New COVID-19 Cases in {country} Over Time")
plt.xlabel("Date")
plt.ylabel("New Cases")
plt.legend()
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

#Plot 2 - New deaths over time in India
plt.figure(figsize=(12, 6))
plt.plot(country_data['date'], country_data['new_deaths'], color='red', label='New Deaths')
plt.title(f"New COVID-19 Deaths in {country} Over Time")
plt.xlabel("Date")
plt.ylabel("New Deaths")
plt.legend()
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()
