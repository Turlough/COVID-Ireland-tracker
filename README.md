# Daily Covid Cases in Ireland

## Summary
A python script that graphs the daily number of new cases and running total
in Ireland. Will migrate to Jupyter notebook soon, to help legibility and thought-flow.

Meanwhile, in the current flow, edit the 'country' parameter in source to chose the datasource and view stats graphically.

I'll hold off on death rates for a bit. There's only so much morbidity I can take right now.

Each commit gets more depressing...

I realise I am going to have to include death rates.

## How to use and edit code
1. Feel free to add to the 'countries' dictionary, but use sources derived from [https://www.worldometers.info/coronavirus/#countries], otherwise you will need to modify the web scraper.
2. On line 19, change the 'country' parameter to view stats for any country int the dictionary.
3. Some countries, like South Korea, have move beyond the exponential model and will no longer graph correctly.
4. Moving beyond the exponential model implies that the situation has peaked in that region and that exponential growth is no longer a good model in that region. That is, infection rates are now under control there. Look at the error message when you select South Korea as country, for example.
5. In this project, countries that have moved from exponential to sigmoid growth are not modelled correctly. It is only good for countries still in the initial exponential-growth stage.


## Sources
Data is scraped from [https://www.worldometers.info/coronavirus/country/ireland/]. This page also shows some useful graphs. Here we scrape the underlying data to calculate extra details like doubling rate.

Take a look at the parent page, [https://www.worldometers.info/coronavirus/#countries]


## Graphs show 
1. Daily new cases
2. Fitted (to best fit exponential) graph of Daily new cases
3. Total cases, the cumulative sum of Daily new cases
4. Fitted (to best fit exponential) graph of Daily new cases

'Fitted' graphs show the best fitting exponential parameters for the underlying data. These parameters are then used to estimate the current doubling rate, which is displayed on the terminal, not the graph. The rule of seventy is used for this estimation.

A note on the doubling rate: Doubling ten times means a thousand-fold increase (1024-fold  to be exact). At the time of writing (26 Mar 2020), the doubling rate for Ireland's total cases is 3.9. This means that in 29 days (i.e. End of April), we can expect that there are a thousand times today's count of 1563- one and a half million, or a quarter of population.

However, take into account:
1. Our testing capacity will have changed significantly during this period. Detection rates depend on testing capacity.
2. A quarter of our population infected might actually be greater than the saturation ratio for infection. This means that daily new infection rate decreases because a significant portion of the population is already infected. In other words, almost everyone who can be infected is already infected.
3. Interesting, we reach this point in about a month's time. With absolute certainly, before early May.

Footnote: Irish population is 4.83 million.

