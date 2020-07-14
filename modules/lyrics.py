"""
@author: Tom Gulliver

Functions for interacting with the lyrics.ovh API
"""

import json
import requests
import urllib.parse

def getLyrics(artist, title):
    """Gets lyrics for a song forom the lyrics API

    Args:
        artist (string): artist name
        title (string): song title

    Returns:
        string: song lyrics
    """    

    # Encode the strings in a http valid format
    artisturi = urllib.parse.quote(artist)
    titleuri = urllib.parse.quote(title)

    # Fixes encoding issue that caused false negative results
    titleuri = titleuri.replace("%E2%80%99" , "%27")
    titleuri = titleuri.replace("%2B", "%26")

    querystring = "https://api.lyrics.ovh/v1/" + artisturi + "/" + titleuri
    req = requests.get(querystring)
    
    if req.status_code != 200 or 'lyrics' not in req.json():
        return ""
    
    return req.json()["lyrics"]


def countWords(lyrics):
    """Counts the lyrics in a string, allowing for line breaks

    Args:
        lyrics (string): the lyrics of a song

    Returns:
        int: word count
    """    
    finallyrics = []
    licenseerror = 32
    licenselyric = "Unfortunately,"

    for line in lyrics.splitlines():
        for word in line.split(" "):
            if word == "":
                continue
            finallyrics.append(word)

    # Checks for lyrics API license issue
    if len(finallyrics) == licenseerror and finallyrics[0]==licenselyric:
        return -1

    return len(finallyrics)
