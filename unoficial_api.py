from ytmusicapi import YTMusic
import json

ytmusic = YTMusic('headers_auth.json')

print('ADD ALL ARTISTS SONGS TO YT MUSIC PLAYLIST\n\n')

artist = input('Type in the artists name: ')

print('\nDo you want to add all songs, or top ones?')
vrsta = input('For all write ALL, for top write TOP: ')

if vrsta == 'TOP':
    top = int(input('\nHow many songs do you want to add? '))

# Create playlist
playlist_id = ytmusic.create_playlist(
    artist, f'Songs from {artist}', 'PRIVATE')

# Get artist's songs
song_ids = []
song_titles = []

artist_id = ytmusic.search(artist, 'artists')[0]['browseId']

artist_info = ytmusic.get_artist(artist_id)['songs']

all_songs = ytmusic.get_playlist(artist_info['browseId'])['tracks']

for song in all_songs:

    if song['title'].lower() in song_titles or 'live' in song['title'].lower():
        continue

    song_titles.append(song['title'].lower())
    song_ids.append(song['videoId'])

if vrsta == 'TOP':
    song_ids = song_ids[0: top]

# Add songs to playlist
ytmusic.add_playlist_items(playlist_id, song_ids)

print(f'\n\nAll {len(song_ids)} songs added')
