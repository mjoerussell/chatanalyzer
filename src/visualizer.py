import matplotlib.pyplot as plt
import calculate_stats as stats

df = stats.get_dataframe()
texts_by_days = stats.get_grouped_texts(df)
totals = texts_by_days.apply(stats.number_of)
totals.index = totals.index.strftime('%m/%d')
totals.plot(kind='bar')
plt.show()
