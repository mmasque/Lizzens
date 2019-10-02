"""Get audio features for each track in list of tracks. 

Last updated on: 2/10/19 by Marcel Masque
"""

import spotipy
import spotipy.util as util
import sys
import pandas as pd
from sklearn.cluster import KMeans

def get_audio_features(tracks, sp):
	"""Get spotify audio features for each track in a list of tracks

	Arguments:

	- tracks: list  of spotify track dictionaries 
	- sp: spotipy.Spotify() instance validated with user token.

	Returns:

	- df: pandas dataframe containing float values from 0-1
		  for a list of audio features for each track. 

	"""
	audio_features = []

	danceability = []
	energy = []
	speechiness = []
	acousticness = []
	instrumentalness = []
	liveness = []
	valence = []

	for i in tracks:
		feature = sp.audio_features(tracks=i['track']['uri'])
		#print(feature)
		audio_features.append(feature)

		#make this pretty someday
		danceability.append(feature[0]['danceability'])
		energy.append(feature[0]['energy'])
		speechiness.append(feature[0]['speechiness'])
		acousticness.append(feature[0]['acousticness'])
		instrumentalness.append(feature[0]['instrumentalness'])
		liveness.append(feature[0]['liveness'])
		valence.append(feature[0]['valence'])

	df = pd.DataFrame({
		'danceability': danceability,
		'energy': energy,	
		'speechiness': speechiness,	
		'acousticness': acousticness, 
		'instrumentalness': instrumentalness,
		'valence': valence
		})
	return df

