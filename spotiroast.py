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

#Returns the user's favorite genres from their favorite artists.
def getTopArtists(client, limit=10):
    topGenres = []
    topArtists = []

    for artist in client.current_user_top_artists(limit=limit)["items"]:
        for genre in artist["genres"]:
            if genre not in topGenres:
                topGenres.append(genre)

        if artist["name"] not in topArtists:
            topArtists.append(artist["name"])

    return topGenres, topArtists

#Return ids for top songs
def getTopTracks(client, limit = 10):
    tracks = []

    for song in client.current_user_top_tracks(limit=limit)["items"]:
        if song["uri"] not in tracks:
            tracks.append(song["uri"])

    return tracks

#Creates playlist using top songs
def createTopPlaylist(client, username, playlistName, topTracks):
    playlist = client.user_playlist_create(username, playlistName)
    playlistID = playlist["id"]
    client.user_playlist_add_tracks(username, playlistID, topTracks)

clientID, clientSecret, redirectURI, username = getCreds("auth.json")
scopes = "playlist-read-private, user-top-read, user-read-recently-played, user-read-private, playlist-modify-public"

client = getClient(scopes, clientID, clientSecret, redirectURI)
topGenres = []
topArtists = []

topGenres, topArtists = getTopArtists(client, limit=5)
print(topArtists)
print(topGenres)

topTracks = getTopTracks(client, limit=20)
print(topTracks)

createTopPlaylist(client, username, "Top Tracks", topTracks)