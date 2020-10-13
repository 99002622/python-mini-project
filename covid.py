def find_top_confirmed(n = 15):
      import pandas as pd
  corona_df = pd.read_csv('covid-19.csv')
  by_country = corona_df.groupby('Country_Region').sum()[['Confirmed', 'Deaths', 'Recovered', 'Active']]
  cdf = by_country.nlargest(n, 'Confirmed')[['Confirmed']]
  return cdf