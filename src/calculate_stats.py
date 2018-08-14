import pandas as pd
import numpy as np 
from datetime import datetime
from xml_converter import XMLConverter

path = "text_analyzer/res/krissy_conversation.xml"
date_parse = '%b %d, %Y %I:%M:%S %p'

def number_of(df):
    return df.shape[0]

def get_texts_from_sender(df, sender):
    is_from_sender = df["type"] == sender
    return df[is_from_sender]

def get_texts_that_contain_string(df, phrase):
    matching_texts = df["body"].str.contains(phrase, na=False)
    return df[matching_texts]

def get_texts_times(df):
    dates = []
    sms_texts = df["tag"] == "sms"
    texts = df[sms_texts]
    timestamps = texts["readable_date"]
    for date in timestamps:
        dates.append(datetime.strptime(date, date_parse))
    return pd.Series(dates)

def get_responding_texts(df):
    diff = df["type"] != df["type"].shift(1).fillna(df["type"])
    return df[diff]

def get_ratio_of_texts(df):
    num_from_krissy = number_of(get_texts_from_sender(df, "1"))
    num_from_me = number_of(get_texts_from_sender(df, "2"))

    total_texts = num_from_krissy + num_from_me

    percent_krissy = num_from_krissy / (total_texts * 1.0)
    percent_me = num_from_me / (total_texts * 1.0)

    return pd.DataFrame({"Person": ["Me", "Krissy"], 
                        "Count": [num_from_me, num_from_krissy],
                        "Percentage": [percent_me, percent_krissy]})

def get_time_deltas(times):
    deltas = [times[i] - times[i - 1] for i in xrange(1, len(times))]
    return pd.Series(deltas)

def get_time_std(df):
    diffs = get_time_deltas(get_texts_times(df).values)
    diffs.std()

def get_texts_from_date(df, date):
    df["readable_date"] = pd.to_datetime(df["readable_date"])
    grouped = df.set_index("readable_date").groupby(pd.Grouper(freq='D'))
    return grouped.get_group(date)

def get_grouped_texts(df):
    df["readable_date"] = pd.to_datetime(df["readable_date"])
    return df.set_index("readable_date").loc["2018-07-24":"2018-08-05"].groupby(pd.Grouper(freq='D'))

def get_dataframe():
    converter = XMLConverter(path)
    return converter.get_dataframe()