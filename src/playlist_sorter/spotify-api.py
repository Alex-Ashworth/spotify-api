import os
import spotipy
from spotipy.oauth2 import SpotifyOAuth
from dotenv import load_dotenv

load_dotenv()

sp = spotipy.Spotify(
    auth_manager=SpotifyOAuth(
        client_id=os.environ["SPOTIFY_CLIENT_ID"],
        client_secret=os.environ["SPOTIFY_CLIENT_SECRET"],
        redirect_uri="http://127.0.0.1:8888/callback",
        scope="playlist-modify-public playlist-read-private playlist-modify-private ugc-image-upload",
    )
)


def auth_test():
    print(sp.current_user_playlists(limit=1))


def run():
    print("Running auth test...")
    auth_test()


run()
