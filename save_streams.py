# -*- coding: utf-8 -*-
"""
Created on Mon Mar  7 10:47:45 2022
@author: OrangeScorpion
"""
import spotipy
import os
from spotipy.oauth2 import SpotifyOAuth
import json

#Location of the folder where data will be saved
local_path = "C:/Users/OrangeScorpion/Documents/SpotifyData/"

# Authorization. I have saved my client ID and secret as environment variables in my Windows user profile, 
# so that this program can only retrieve my data if it is run from my personal computer while I am logged in as admin.
# Your client ID and secret are provided through the Spotify Developers website
scope = "user-read-recently-played"
client_id = os.environ.get("sp_client_id") #environment variables
client_secret = os.environ.get("sp_client_secret") #environment variables
redirect_url= "http://localhost:8080"

sp = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id=client_id, 
                                               client_secret= client_secret, 
                                               redirect_uri=redirect_url, 
                                               scope=scope))

#count files in directory to index and create a name for the file to be saved.
path, dirs, files = next(os.walk(local_path))
file_count = len(files)

file_name = "sample"+str(file_count+1)+".json"

#This sends the API request with the authorisation when called. The default and maximum limit is 50, but you can specify a lesser limit.
results = sp.current_user_recently_played(limit = 50)

#Request and save data
with open(local_path+file_name, "w") as outfile:
    json.dump(results, outfile)
