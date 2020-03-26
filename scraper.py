import requests
from bs4 import BeautifulSoup
import pandas as pd 
import re
import numpy as np
from scipy.optimize import curve_fit
import matplotlib.pyplot as plt

countries = {
	'Ireland': 		'https://www.worldometers.info/coronavirus/country/ireland/',
	'UK': 			'https://www.worldometers.info/coronavirus/country/uk/',
	'USA': 			'https://www.worldometers.info/coronavirus/country/us/',
	'Italy': 		'https://www.worldometers.info/coronavirus/country/italy/',
	'South Korea': 	'https://www.worldometers.info/coronavirus/country/south-korea',
	'Poland':		'https://www.worldometers.info/coronavirus/country/poland/',
	'China':		'https://www.worldometers.info/coronavirus/country/china/'
}
# Choose country here...
country = 'Ireland'
url = countries[country]

content = requests.get(url).text
soup = BeautifulSoup(content, features='html.parser')


####### FUNCTIONS AND LAMBDAS ###############
#-------------------------------------------#


# The function to fit datapoints to is exponential
def exponential(x, a, b, c):
    """Return values from a general exponential function."""
    return a * np.exp(b * x) + c

# Approx doubling rate, to one decimal place, using the rule of 70 (72 actually)
doubling = lambda x: '{:.1f}'.format(0.72/x)


##############################################

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

popt1, pcov1 = curve_fit(exponential, df.index, df.DailyIncrease)
popt2, pcov2 = curve_fit(exponential, df.index, df.Total)

# Display the data
print(df)
print()

# Rule of 70 (72 is used instead)
print('Doubling rate of daily cases', doubling(popt1[1]))
print('Doubling rate of total cases', doubling(popt2[1]))


# Plot the data
plt.plot(df.DailyIncrease, color = '#800', label = 'Daily Increase')
plt.plot(exponential(df.index, *popt1), 'r-', color = '#FDD', label = 'Daily Increase (smooth)')

plt.plot(df.Total, color = '#088', label = 'Total Cases')
plt.plot(exponential(df.index, *popt2), 'r-',color = '#DFF', label = 'Total (smooth)')

plt.title(country)
plt.legend()
plt.grid()
plt.xlabel('Day')
plt.ylabel('Count')
plt.show()
