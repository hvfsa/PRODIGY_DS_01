import pandas as pd
import matplotlib.pyplot as plt

# Load the data
data = pd.read_csv("population_2023.csv")

# Display the first few rows to check if the data is loaded correctly
print(data.head())

# Create a bar chart for the top 10 most populous countries
top_10 = data.head(10)

plt.figure(figsize=(14, 7))
plt.bar(top_10['Country'], top_10['Population (thousands)'], color='skyblue')
plt.xlabel('Country')
plt.ylabel('Population (thousands)')
plt.title('Top 10 Most Populous Countries in 2023')
plt.xticks(rotation=45)
plt.show()
