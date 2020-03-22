import requests
from bs4 import BeautifulSoup
import pandas as pd 
import re
import matplotlib.pyplot as plt

url = 'https://www.worldometers.info/coronavirus/country/ireland/'
content = requests.get(url).text

soup = BeautifulSoup(content, features='html.parser')
script = soup.find('div', id='graph-cases-daily').findNext('script')
# print(script.text)
lines = script.text.split('\n')
datas = [l for l in lines if l.strip().startswith('data')]
data = datas[0].strip()
# print(data)

counts_text = re.findall('[0-9]+', data)
counts = list(map(int, counts_text))
print(counts)

df = pd.DataFrame(counts, columns=['DailyIncrease'])
df['Total'] = df.DailyIncrease.cumsum()
print(df)

di = df.DailyIncrease
tot = df.Total

plt.plot(di, label = 'Daily Increase')
plt.plot(tot, label = 'Total Cases')
plt.title('Ireland')
plt.legend()
plt.grid()
plt.xlabel('Day')
plt.ylabel('Count')
plt.show()



