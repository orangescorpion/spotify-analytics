# spotify-analytics

## Description
An ETL pipeline for collecting user streaming data from the Spotify API

Publishing code snippets as this project progresses, currently the ET part of the ETL is up :) A script that authorises and saves raw json data from the Spotify API, and a script that converts this json file into two CSV files: metadata and individual streaming data.

## Instructions
Run save_streams.py using appropriate local variables, followed by jsonToCSV.py

Following this, the user's 50 most recent music streams are requested from the Spotify API, the original json file is saved, and then opened and converted to csv files.

## TODO
The next script which I am currently working on creates the SQL database and loads the requests. Following this, I will have an ETL pipeline to mine my streaming data and store it. 

Then, I'll be able to create some cool dashboards, maybe do some seasonal-trend analysis to see if anything interesting appears, and investigate Spotify's reccommendations based on features I tend to gravitate to.
