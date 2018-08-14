import pandas as pd
import numpy as np 
from datetime import datetime
from xml_converter import XMLConverter

path = "text_analyzer/res/krissy_conversation.xml"
date_parse = '%b %d, %Y %I:%M:%S %p'

def getNumberOfTexts(sender):
    converter = XMLConverter(path)
    texts_by_types = converter.get_dataframe()
    is_from_sender = texts_by_types[converter.sender] == sender
    return texts_by_types[is_from_sender].shape[0]

def getTextsThatContainString(phrase):
    converter = XMLConverter(path)
    texts = converter.get_dataframe()
    matching_texts = texts[converter.text].str.contains(phrase, na=False)
    return texts[matching_texts].shape[0]

def get_texts_times():
    converter = XMLConverter(path)
    dates = []
    texts = converter.get_dataframe()
    sms_texts = texts[converter.message_type] == "sms"
    texts = texts[sms_texts]
    timestamps = texts[converter.timestamp]
    for date in timestamps:
        dates.append(datetime.strptime(date, date_parse))
    return dates

def getRatioOfTexts():
    num_from_krissy = getNumberOfTexts("1")
    num_from_me = getNumberOfTexts("2")

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
print(max(get_time_deltas(get_texts_times())))