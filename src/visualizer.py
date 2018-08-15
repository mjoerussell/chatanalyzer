import matplotlib.pyplot as plt
import pandas as pd
import calculate_stats as stats

df = stats.get_dataframe()


def texts_per_day(df):
    texts_by_days = stats.get_grouped_texts(df)
    day_totals = texts_by_days.apply(stats.number_of)
    day_totals.index = day_totals.index.strftime('%m/%d')
    return day_totals

def texts_per_hour(df):
    df["readable_date"] = pd.to_datetime(df["readable_date"])
    times = pd.DatetimeIndex(df["readable_date"])
    hour_totals = df.groupby([times.hour]).apply(stats.number_of)
    return hour_totals

def average_texts_per_hour(df):
    pass

plt.figure(1)

plt.subplot("121")
plt.title("Texts per Day")
texts_per_day(df).plot(kind='bar')

plt.subplot("122")
plt.title("Texts per Hour")
texts_per_hour(df).plot(kind='bar')

# plt.subplot("123")
# plt.title("Average Texts per Hour")


plt.show()

