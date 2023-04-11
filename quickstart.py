import os
import spotipy
from spotipy.oauth2 import SpotifyOAuth
from spotipy.util import CLIENT_CREDS_ENV_VARS

#alt method for creds
os.environ["SPOTIPY_CLIENT_ID"] = "9189294878b349208c53d979e331073d"
os.environ["SPOTIPY_CLIENT_SECRET"] = "838724677a564c1d8f6a3337d831646c"
os.environ["SPOTIPY_REDIRECT_URI"] = "http://localhost:8888/callback/"

scope = "user-library-read, playlist-read-private, user-read-private, user-read-playback-position, user-read-recently-played, user-top-read"

sp = spotipy.Spotify(auth_manager=SpotifyOAuth(scope=scope))

results = sp.current_user_saved_tracks()
for idx, item in enumerate(results['items']):
    track = item['track']
    print(idx, track['artists'][0]['name'], " – ", track['name'])
