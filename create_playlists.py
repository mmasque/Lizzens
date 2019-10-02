"""Create 10 playlists based on Kmeans clustering of 
audio features of songs.

Last updated on: 2/10/19 by Marcel Masque

Usage: 
	- Terminal: python create_playlists.py <spotify_username>
	- Make sure to have set 
		SPOTIPY_CLIENT_ID, 
		SPOTIPY_CLIENT_SECRET, 
		SPOTIPY_REDIRECT_URI
"""


import spotipy
from sklearn.cluster import KMeans
from get_audio_features import get_audio_features
from import_data import startup
from import_data import get_liked_songs

N_CLUSTERS = 10
username, token = startup('playlist-modify-public user-library-read')
if token:
	sp = spotipy.Spotify(auth=token)
	tracks = get_liked_songs(sp)
	df = get_audio_features(tracks, sp)
	kmeans = KMeans(n_clusters = N_CLUSTERS).fit(df)

	for i in range(N_CLUSTERS):
		songs = []
		for j in range(len(kmeans.labels_)):
			if kmeans.labels_[j] == i:
				songs.append(tracks[j]['track']['uri'])

		info = sp.user_playlist_create(username, str(i), public=True, description="Automatically created playlist")
		i_d = info['id']
		sp.user_playlist_add_tracks(username, i_d, songs)
else:
	print("Could not get token for ", username)


