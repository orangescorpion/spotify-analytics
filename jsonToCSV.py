# -*- coding: utf-8 -*-
"""
Created on Mon Mar 21 17:02:09 2022
@author: OrangeScorpion
"""
#imports
import pandas as pd
from pandas import DataFrame as df
import json
from datetime import datetime
import tzlocal
import os

#Location of json data
raw_path = "C:/Users/Olivia/Documents/DE Projects/Spotify API/Data Files/raw_data/json/"

# Where the metadata and streams will be saved
csv_path = "C:/Users/OrangeScorpion/Documents/metadata/"
csv_path2 = "C:/Users/OrangeScorpion/Documents/streams/"

local_timezone = tzlocal.get_localzone() # get pytz timezone

# Get the name of the most recent data file that was saved (based off the naming convention I've used.) Otherwise specify a file name
path, dirs, files = next(os.walk(raw_path))
file_count = len(files)
file = "sample"+str(file_count)+".json"

# Open json file
f = open(raw_path+file)
results = json.load(f)

#get list of tracks listened to (streams)
items = results['items'] #track list

#get metadata
next2 = results['next'] #next
href = results['href'] #href
limit = results['limit'] #size limit on api call

cursors = results['cursors'] #time limits on api call
after=int(cursors['after'])/1000 #time limits on api call
before=int(cursors['before'])/1000 #time limits on api call
lt_before = datetime.fromtimestamp(float(before), local_timezone) #local datetime
lt_after = datetime.fromtimestamp(float(after), local_timezone) #local datetime

# initialize list of lists
data = [[href, next2, str(limit), 
        lt_before.strftime("%m/%d/%Y"),
        lt_after.strftime("%m/%d/%Y"),
        lt_before.strftime("%H:%M:%S"),
        lt_after.strftime("%H:%M:%S"),]]

# Create pandas DataFrame for metadata and save to CSV
dataframe = df(data, columns = ['href', 'next', 'limit',
                                'date_before', 'date_after',
                                'time_before', 'time_after'])

df.to_csv(dataframe, csv_path+file+"_metadata.csv")

# create normalised json for streams and save to CSV
normalised = pd.json_normalize(items)
df.to_csv(normalised, csv_path2+file+"_listening.csv") #save
