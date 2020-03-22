import requests
from bs4 import BeautifulSoup
import pandas as pd 
import re
import matplotlib.pyplot as plt

url = 'https://www.worldometers.info/coronavirus/country/ireland/'
content = requests.get(url).text
soup = BeautifulSoup(content, features='html.parser')

# Find the script element following div with id 'graph-cases-daily'
script = soup.find('div', id='graph-cases-daily').findNext('script')
# Find the data line
lines = script.text.split('\n')
datas = [l for l in lines if l.strip().startswith('data')]
data_line = datas[0].strip()
# Extract the data from the data_line
counts_text = re.findall('[0-9]+', data_line)
counts = list(map(int, counts_text))
# Create DataFrame with Cumulative Sum of the daily data
df = pd.DataFrame(counts, columns=['DailyIncrease'])
df['Total'] = df.DailyIncrease.cumsum()

# Display the data
print(df)
# Plot the data
plt.plot(df.DailyIncrease, label = 'Daily Increase')
plt.plot(df.Total, label = 'Total Cases')
plt.title('Ireland')
plt.legend()
plt.grid()
plt.xlabel('Day')
plt.ylabel('Count')
plt.show()



