import sys
import spotipy
import spotipy.util as util
from copy import deepcopy

def startup(scope):
	"""take username from args and get spotify token 
	   to access spotify account

	Arguments: 

	- scope: str that determines scope of access to spotify account

	Returns:

	- username: str, username of spotify account to access
	- token: str, for use in call to spotipy.Spotify()
	 to access spotify account.

	"""
	if len(sys.argv) > 1:
		username = sys.argv[1]
	else:
		print("Usage: " +sys.argv[0]+ " username")
		sys.exit()

	token = util.prompt_for_user_token(username, scope)

	return username, token

def get_liked_songs(sp):
	"""get list of liked songs from account instance sp

	Arguments:

	- sp: instance of spotipy.Spotify()

	Returns: 

	- tracks: list of track dictionaries. 
	"""
	results = sp.current_user_saved_tracks(limit=50)
	tracks = results['items']
	while results['next']:
		results = sp.next(results)
		tracks.extend(results['items'])
	return tracks

