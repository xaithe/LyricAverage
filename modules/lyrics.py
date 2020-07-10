import json
import requests
import urllib.parse

def getLyrics(artist, title):
    """[summary]

    Args:
        artist ([type]): [description]
        title ([type]): [description]

    Returns:
        [type]: [description]
    """    

    artisturi = urllib.parse.quote(artist)
    titleuri = urllib.parse.quote(title)
    titleuri = titleuri.replace("%E2%80%99" , "%27")
    titleuri = titleuri.replace("%2B", "%26")

    querystring = "https://api.lyrics.ovh/v1/" + artisturi + "/" + titleuri
    req = requests.get(querystring)
    
    if req.status_code != 200 or 'lyrics' not in req.json():
        return ""
    
    return req.json()["lyrics"]

def removeNewlines(lyrics):
    """[summary]

    Args:
        lyrics ([type]): [description]

    Returns:
        [type]: [description]
    """    

    lyrics = lyrics.replace("\\n\\n", " ")
    lyrics = lyrics.replace("\\n", " ")
    lyrics = lyrics.replace("\\r", " ")

    return lyrics

def countWords(lyrics):
    """[summary]

    Args:
        lyrics ([type]): [description]

    Returns:
        [type]: [description]
    """    

    words = removeNewlines(lyrics).split()
    
    if len(words) == 32 and words[0]=="Unfortunately,":
        return -1

    return len(words)
