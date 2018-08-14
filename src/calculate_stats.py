import pandas as pd
import numpy as np 
from datetime import datetime
from xml_converter import XMLConverter

path = "text_analyzer/res/krissy_conversation.xml"
date_parse = '%b %d, %Y %I:%M:%S %p'

def number_of(texts):
    return texts.shape[0]

def get_texts_from_sender(df, sender):
    is_from_sender = df[converter.sender] == sender
    return df[is_from_sender]

def get_texts_that_contain_string(df, phrase):
    matching_texts = df[converter.text].str.contains(phrase, na=False)
    return df[matching_texts]

def get_texts_times(df):
    dates = []
    sms_texts = df[converter.message_type] == "sms"
    texts = df[sms_texts]
    timestamps = texts[converter.timestamp]
    for date in timestamps:
        dates.append(datetime.strptime(date, date_parse))
    return dates

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
    return deltas

#print(getRatioOfTexts())
converter = XMLConverter(path)
df = converter.get_dataframe()
print(max(get_time_deltas(get_texts_times(get_texts_that_contain_string(df, "love you")))))