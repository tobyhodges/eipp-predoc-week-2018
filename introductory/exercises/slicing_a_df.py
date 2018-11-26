#     1. Do the two statements below produce the same output?
#     2. Based on this, what rule governs what is included (or not) in numerical
#        slices and named slices in Pandas?

print(data.iloc[0:2, 0:2])
print(data.loc['Albania':'Belgium', 'gdpPercap_1952':'gdpPercap_1962'])
