import spotipy as sp
from spotipy import util
from spotipy.oauth2 import SpotifyOAuth

#retrieves creds from auth file.
def getCreds(fileName):
    auth = open(fileName, "r").readlines()

    clientID = auth[1].split(" ")[1].replace('"', "")

    clientSecret = auth[2].split(" ")[1].replace('"', "")

    redirectURI = auth[3].split(" ")[1].replace('"', "")
    
    username = auth[4].split(" ")[1].replace('"', "").replace("\n", "")

    return clientID, clientSecret, redirectURI, username

#Returns a Spotify client with the given scopes.
def getClient(scopes, clientID, clientSecret, redirectURI):
    authorizer = SpotifyOAuth(client_id=clientID, client_secret=clientSecret, redirect_uri=redirectURI, scope=scopes)

    return sp.Spotify(oauth_manager=authorizer)

clientID, clientSecret, redirectURI, _ = getCreds("auth.json")

scopes = "playlist-read-private, user-top-read, user-read-recently-played, user-read-private, playlist-modify-public"

client = getClient(scopes, clientID, clientSecret, redirectURI)

print(client.current_user_top_artists())