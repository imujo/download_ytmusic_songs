# download_ytmusic_songs
This is a Python app for locally storing all songs from an artist on YT Music

API Credit: https://ytmusicapi.readthedocs.io/en/latest/index.html

## SETUP

You need to create a file called *headers_auth.json* with the following format:
```
{
    "User-Agent": "USER AGENT",
    "Accept": "*/*",
    "Accept-Language": "en-US,en;q=0.5",
    "Content-Type": "application/json",
    "X-Goog-AuthUser": "0",
    "x-origin": "https://music.youtube.com",
    "Cookie" : "PASTE_COOKIE"
}

```

To find your USER AGENT just google *What is my user agent?*

To find the COOKIE, follow the [Copy authentication headers](https://ytmusicapi.readthedocs.io/en/latest/setup.html#copy-authentication-headers) on the Youtube Music Api website.
Copy the cookie and paste it in the json file.


## USAGE

Now you can run the app. You will be propted to write the artists name and whether you want to add all songs or just some. After the script is completed, you will have a new playlist in your Youtube Music. 
From then you can easily download the songs by right-clicking on the playlist and selecting download.

Note that you need YT Music Premium to download songs.
