# Fill in the blanks below to plot the minimum GDP per capita over time for all
# the countries in Europe. Modify it again to plot the maximum GDP per capita
# over time for Europe.

data_europe = pandas.read_csv('data/gapminder_gdp_europe.csv', index_col='country')
data_europe.____.plot(label='min')
data_europe.____
plt.legend(loc='best')
plt.xticks(rotation=90)
