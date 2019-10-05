# Lizzens

Create 10 playlists from a Spotify user's Liked Songs based on the songs' audio features.

## Getting Started

Clone the repo with https://github.com/mmasque/Lizzens.git


You'll need to setup authorised requests to see Liked Songs and create playlists on your Spotify account.

See https://spotipy.readthedocs.io/en/latest/#authorized-requests for more info. 


### Prerequisites

This project uses Spotipy, a python library for the Spotify API. 

To install it, enter the following in terminal: 

```
pip install spotipy
```
or 
```
easy_install install spotipy
```
Or you can get the source from github at https://github.com/plamere/spotipy

You'll also need **pandas** and **scikit-learn.** 

Install pandas: https://pandas.pydata.org/pandas-docs/stable/install.html

Install scikit-learn: https://scikit-learn.org/stable/install.html


## Running the project

Simply run

```
python create_playlists.py <spotify_username>
```

once you've setup authorised requests and installed the libraries. 

## Acknowledgments

* @plamere for spotipy
* a note: this is not new. It has been done before: Organize Your Music is a user friendly app that does this, and more: http://organizeyourmusic.playlistmachinery.com/ 


