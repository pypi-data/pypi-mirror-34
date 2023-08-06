import numpy as np
import pandas as pd
import os
from os import makedirs, path as op

def color_tones(tone_float):
    return 'negative' if tone_float < 0 else 'positive'

def process_files():
    csvs = [op.join(os.getcwd(), f) for f in os.listdir('.') if f.endswith('.export.csv')]
    schema = pd.read_csv('v2_events_schema.csv')
    column_names = schema['tableId']
    files = []
    for csv in csvs:
      events = pd.read_csv(csv, names = list(column_names), delimiter='\t')
      events['fillKey'] = events.apply(lambda row: color_tones(row['AvgTone']), axis=1)
      filename = csv.replace('.export.csv', '.tone_location.export.csv')
      tone_and_loc = events[['fillKey', 'NumMentions', 'ActionGeo_Lat', 'ActionGeo_Long', 'AvgTone', 'SOURCEURL']].dropna()
      tone_and_loc.columns = ['fillKey', 'radius', 'latitude', 'longitude', 'AvgTone', 'SOURCEURL']
      tone_and_loc.to_json(filename, orient='records')
      files.append(filename)
    return files
